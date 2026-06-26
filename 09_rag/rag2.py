from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 임베딩 모델 로드 (한국어 지원)
print("모델 로딩 중...")
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
print("모델 로드 완료\n")

# 1단계: 문서 로드 + 청크 분리
def load_chunks(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return [c.strip() for c in text.split("\n\n") if c.strip()]

# 2단계: 청크를 벡터로 변환
def embed_chunks(chunks):
    return model.encode(chunks)

# 3단계: 질문과 가장 유사한 청크 찾기
def find_relevant(query, chunks, chunk_embeddings, top_k=1):
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, chunk_embeddings)[0]
    top_index = scores.argsort()[-top_k:][::-1]
    print(f"  [유사도 점수] {[(chunks[i][:15], round(scores[i], 2)) for i in top_index]}")
    return [chunks[i] for i in top_index]

# 4단계: Groq에 전달
def ask(question, chunks, chunk_embeddings):
    relevant = find_relevant(question, chunks, chunk_embeddings)
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
chunk_embeddings = embed_chunks(chunks)
print(f"총 {len(chunks)}개 청크 임베딩 완료\n")

questions = [
    "휴가는 몇 일이야?",
    "월급 날이 언제야?",
    "집에서 일할 수 있어?",
    "주식 옵션은 어떻게 돼?"
]

for q in questions:
    print(f"Q: {q}")
    answer = ask(q, chunks, chunk_embeddings)
    print(f"A: {answer}\n")
