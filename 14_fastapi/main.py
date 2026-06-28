from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 대화 기록 저장소 (서버 메모리에 저장)
# { "김철수": [{"role": "user", ...}, {"role": "assistant", ...}] }
conversations = {}

class QuestionRequest(BaseModel):
    question: str
    user_name: str = "익명"

@app.get("/")
def home():
    return {"message": "FastAPI + Groq AI 서버"}

@app.post("/ask")
def ask(request: QuestionRequest):
    # 이 사용자의 기록이 없으면 빈 리스트로 시작
    if request.user_name not in conversations:
        conversations[request.user_name] = []

    # 사용자 메시지 기록에 추가
    conversations[request.user_name].append({
        "role": "user",
        "content": request.question
    })

    # Groq에 시스템 메시지 + 전체 대화 기록 전달
    messages = [{"role": "system", "content": "한국어로만 짧게 답해."}] \
             + conversations[request.user_name]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    answer = response.choices[0].message.content

    # AI 답변도 기록에 추가
    conversations[request.user_name].append({
        "role": "assistant",
        "content": answer
    })

    return {
        "질문한사람": request.user_name,
        "질문": request.question,
        "AI답변": answer,
        "총대화횟수": len([m for m in conversations[request.user_name] if m["role"] == "user"])
    }

@app.get("/history/{user_name}")
def get_history(user_name: str):
    if user_name not in conversations:
        return {"message": f"{user_name}의 대화 기록이 없습니다."}
    return {"사용자": user_name, "대화기록": conversations[user_name]}

@app.delete("/history/{user_name}")
def clear_history(user_name: str):
    if user_name in conversations:
        conversations[user_name] = []
    return {"message": f"{user_name}의 대화 기록을 초기화했습니다."}
