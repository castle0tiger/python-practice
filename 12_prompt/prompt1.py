from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(system, user):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    )
    return response.choices[0].message.content

question = "파이썬 리스트가 뭐야?"

# 1. 시스템 프롬프트 없음
print("=== 프롬프트 없음 ===")
print(ask("", question))

print("\n=== 초등학생용 ===")
print(ask("너는 초등학생에게 설명하는 선생님이야. 쉬운 단어만 써.", question))

print("\n=== 개발자용 ===")
print(ask("너는 시니어 개발자야. 기술적으로 정확하게 설명해.", question))

print("\n=== Few-shot (형식 지정) ===")
print(ask("""
사용자가 Python 개념을 물어보면 아래 형식으로만 답해.

[개념]: 한 줄 정의
[예시]: 코드 한 줄
[핵심]: 기억할 점 한 줄

다른 설명은 절대 추가하지 마.
""", "파이썬 딕셔너리가 뭐야?"))

print("\n=== Chain of Thought ===")
print(ask(
    "문제를 풀 때 반드시 단계별로 생각하고, 각 단계를 번호로 보여줘.",
    "판다스로 CSV 파일을 읽어서 나이가 30 이상인 사람만 필터링하려면 어떻게 해야 해?"
))

print("\n=== Chain of Thought ===")
print(ask(
    "문제를 풀 때 반드시 단계별로 생각하고, 각 단계를 번호로 보여줘.",
    "판다스로 CSV 파일을 읽어서 나이가 30 이상인 사람만 필터링하려면 어떻게 해야 해?"
))
