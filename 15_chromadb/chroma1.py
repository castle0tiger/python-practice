import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 1. ChromaDB 클라이언트 — 데이터를 파일로 저장 (서버 꺼도 유지)
client = chromadb.PersistentClient(
    path=os.path.join(os.path.dirname(__file__), "chroma_db")
)

# 2. 임베딩 모델 지정 — rag2.py에서 쓴 것과 동일한 모델
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

# 3. 컬렉션 생성 — DB의 "테이블" 같은 것
collection = client.get_or_create_collection(
    name="company_rules",
    embedding_function=embedding_fn
)

# 4. 문서 로드 & 청크 분리
rules_path = os.path.join(os.path.dirname(__file__), "..", "09_rag", "company_rules.txt")
with open(rules_path, encoding="utf-8") as f:
    chunks = [c.strip() for c in f.read().split("\n\n") if c.strip()]

# 5. DB에 저장 (이미 있으면 건너뜀)
existing = collection.count()
if existing == 0:
    collection.add(
        documents=chunks,
        ids=[f"doc{i}" for i in range(len(chunks))]
    )
    print(f"DB에 {len(chunks)}개 청크 저장 완료")
else:
    print(f"DB에 이미 {existing}개 청크 있음 — 저장 건너뜀")

# 6. 질문 → DB 검색 → Groq 답변
questions = ["연차는 며칠이야?", "급여는 언제 줘?", "재택근무 가능해?"]

for question in questions:
    # ChromaDB가 유사한 청크 자동 검색
    results = collection.query(query_texts=[question], n_results=2)
    context = "\n".join(results["documents"][0])

    response = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "한국어로만 짧게 답해."},
            {"role": "user", "content": f"참고 문서:\n{context}\n\n질문: {question}"}
        ]
    )
    print(f"\nQ: {question}")
    print(f"A: {response.choices[0].message.content}")
