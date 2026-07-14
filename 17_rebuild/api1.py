from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from groq import Groq
from dotenv import load_dotenv
import os

class RegisterRequest(BaseModel):
    name: str           # 문자열, 필수
    score: int          # 정수, 필수
    absence: int = 0   # 정수, 선택(기본값 = 0)

class AskRequest(BaseModel):
    question: str # 문자열, 필수
    

app = FastAPI()

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
api_key = os.getenv("GROQ_API_KEY") 

client = Groq(api_key=api_key)

groq_memory = []  #대화내용 기록 리스트


@app.get("/")
def get_home():
    return {"이름": "캐슬타이거", "목표": ["파이썬 입문", "코드 작성 및 이해", "AI에 대한 기술적 학습(기초)"]}


@app.get("/scores")
def get_scores():
    scores = [85, 75, 95, 65, 90]
    total = 0
    
    for s in scores:
        total += s

    average = total / len(scores)

    return {"개수": len(scores), "총합": total, "평균": average}


@app.post("/register")
def post_register(register: RegisterRequest):
    if register.score >= 80 and register.absence <= 2:
        result = "합격"
    else: 
        result = "불합격"    
        
    return {"이름": register.name, "점수": register.score, "판정": result}


@app.get("/page")
def get_page():
    return FileResponse("17_rebuild/chat.html")


@app.post("/ask")
def post_ask(request: AskRequest):
    groq_memory.append({"role": "user", "content": request.question})
    script = [{"role": "system", "content": "한국어로 3 문장으로 답해"}] + groq_memory
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages= script
    )

    groq_answer = response.choices[0].message.content
    groq_memory.append({"role": "assistant", "content": groq_answer})
    return {"질문": request.question, "답변": groq_answer, "누적대화수": len(groq_memory)}