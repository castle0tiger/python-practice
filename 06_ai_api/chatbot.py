from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation = []

@app.route("/")
def home():
    return render_template("chat.html", conversation=conversation)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation
    )

    answer = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": answer})

    return render_template("chat.html", conversation=conversation)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)
