from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 1단계: 문서를 청크(조각)로 분리
def load_chunks(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
    return chunks

# 2단계: 질문과 관련된 청크 찾기
def find_relevant(query, chunks):
    query_words = set(query.replace("?", "").split())
    scored = []
    for chunk in chunks:
        # 앞 2글자만 비교 → "연차가"→"연차", "연차는"→"연차" 둘 다 매칭
        score = sum(1 for w in query_words if len(w) >= 2 and w[:2] in chunk)
        scored.append((score, chunk))
    scored.sort(reverse=True)
    return [chunk for score, chunk in scored[:2] if score > 0]


# 3단계: 관련 내용 + 질문을 AI에게 전달
def ask(question, chunks):
    relevant = find_relevant(question, chunks)
    if not relevant:
        context = "관련 문서를 찾지 못했습니다."
    else:
        context = "\n\n".join(relevant)

    prompt = f"""아래 회사 문서를 참고해서 질문에 답해줘. 문서에 없는 내용은 모른다고 해.

문서:
{context}

질문: {question}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 실행
chunks = load_chunks(os.path.join(SCRIPT_DIR, "company_rules.txt"))
print(f"총 {len(chunks)}개 청크 로드됨\n")

questions = [
    "연차가 몇 일이야?",
    "급여는 언제 받아?",
    "재택근무 며칠이나 할 수 있어?",
    "주식 옵션은 어떻게 돼?"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {ask(q, chunks)}")
    print()
