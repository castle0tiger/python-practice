from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation = [
    {"role": "system", "content": "You are a helpful assistant. IMPORTANT: Always respond in Korean only. Never mix in English, Japanese, Russian, Chinese, or any other language. 100% Korean responses only."}
]

@app.route("/")
def home():
    return render_template("chat.html", conversation=conversation)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    conversation.append({"role": "user", "content": user_input})

    # 모델에 보낼 때만 한국어 지시 추가 (저장된 대화에는 영향 없음)
    messages_to_send = conversation[:-1] + [
        {"role": "user", "content": user_input + "\n\n(반드시 한국어로만 답변하세요)"}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages_to_send
    )

    answer = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": answer})

    return render_template("chat.html", conversation=conversation)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)
