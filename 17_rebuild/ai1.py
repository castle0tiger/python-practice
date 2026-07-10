from groq import Groq 
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "한국어로 3 문장으로 답해"},
        {"role": "user", "content": "한국에서 가장 유명한 연예인은 누구야?"}
    ]
)

groq_answer = response.choices[0].message.content
print(groq_answer)