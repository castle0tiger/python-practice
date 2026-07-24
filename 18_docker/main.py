from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Docker 컨테이너에서 실행 중!", "made_by": "캐슬타이거"}
