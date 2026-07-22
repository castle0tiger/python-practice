# 모듈 불러오기
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os


# STEP 1 — 문서 읽고 청크로 나누기 (지도: "문서 → 청크 분리")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rules_path = os.path.join(SCRIPT_DIR, "..", "09_rag", "company_rules.txt")

with open(rules_path, encoding="utf-8") as f:
    text = f.read()

chunks = text.split("\n\n")


# STEP 2 — ChromaDB 준비 + 청크 저장 (지도: "임베딩 → ChromaDB에 저장")
client_db = chromadb.Client()

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

collection = client_db.create_collection(
    name = "company_rules",
    embedding_function = embedding_fn
)

collection.add(
    documents = chunks,
    ids = [str(i) for i in range(len(chunks))]
)


# STEP 3 — 질문으로 검색 (지도: "질문 → ChromaDB가 가까운 청크 찾아줌")
question = "연차 며칠 쓸 수 있어?"

results = collection.query(
    query_texts=[question],
    n_results=1
)

found_chunk = results["documents"][0][0]
print("찾은 청크:", found_chunk)


# STEP 4 — 청크 + 질문 → Groq 답변 (지도: "청크+질문을 AI에 → 답변")
load_dotenv(dotenv_path=os.path.join(SCRIPT_DIR, "..", ".env"))
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client_groq.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "아래 회사 규정을 근거로만 한국어로 답해."},
        {"role": "user", "content": f"[규정]\n{found_chunk}\n\n[질문]\n{question}"}
    ]
)

print("\nAI 답변:", response.choices[0].message.content)