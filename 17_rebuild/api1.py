from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

class RegisterRequest(BaseModel):
    name: str           # 문자열, 필수
    score: int          # 정수, 필수
    absence: int = 0   # 정수, 선택(기본값 = 0)

app = FastAPI()

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
