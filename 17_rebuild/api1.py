from fastapi import FastAPI

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
