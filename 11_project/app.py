from flask import Flask, render_template, request
from groq import Groq
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# RAG 모델 로드
print("모델 로딩 중...")
embed_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def load_chunks():
    with open(os.path.join(SCRIPT_DIR, "knowledge.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    return [c.strip() for c in text.split("\n\n") if c.strip()]

chunks = load_chunks()
chunk_embeddings = embed_model.encode(chunks)
print(f"지식베이스 로드 완료: {len(chunks)}개 청크\n")

# SQLite 초기화
def init_db():
    conn = sqlite3.connect(os.path.join(SCRIPT_DIR, "chat_history.db"))
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(role, content):
    conn = sqlite3.connect(os.path.join(SCRIPT_DIR, "chat_history.db"))
    cur = conn.cursor()
    cur.execute("INSERT INTO history (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(os.path.join(SCRIPT_DIR, "chat_history.db"))
    cur = conn.cursor()
    cur.execute("SELECT role, content FROM history ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [{"role": r, "content": c} for r, c in rows]

# RAG 검색
def find_relevant(query):
    query_embedding = embed_model.encode([query])
    scores = cosine_similarity(query_embedding, chunk_embeddings)[0]
    top_indices = scores.argsort()[-2:][::-1]
    return "\n\n".join([chunks[i] for i in top_indices])

@app.route("/")
def home():
    return render_template("index.html", conversation=get_history())

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    context = find_relevant(user_input)
    history = get_history()

    messages = [
        {"role": "system", "content": "You are a Python learning assistant. Answer based on the provided document. Always respond in Korean only."}
    ] + history + [
        {"role": "user", "content": f"참고 문서:\n{context}\n\n질문: {user_input}\n\n(반드시 한국어로만 답변하세요)"}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    answer = response.choices[0].message.content

    save_message("user", user_input)
    save_message("assistant", answer)

    return render_template("index.html", conversation=get_history())

@app.route("/clear", methods=["POST"])
def clear():
    conn = sqlite3.connect(os.path.join(SCRIPT_DIR, "chat_history.db"))
    cur = conn.cursor()
    cur.execute("DELETE FROM history")
    conn.commit()
    conn.close()
    return render_template("index.html", conversation=[])

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5003))
    app.run(debug=True, port=port, host="0.0.0.0")
