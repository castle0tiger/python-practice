from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# LLM 설정
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# 기존 방식 (Groq 직접 호출)
print("=== 기존 방식 ===")
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "한국어로만 답해"},
        {"role": "user", "content": "판다스가 뭐야? 한 줄로"}
    ]
)
print(response.choices[0].message.content)

# LangChain 방식
print("\n=== LangChain 방식 ===")
messages = [
    SystemMessage("한국어로만 답해"),
    HumanMessage("판다스가 뭐야? 한 줄로")
]
response = llm.invoke(messages)
print(response.content)


from langchain_core.prompts import ChatPromptTemplate

print("\n=== Chain (프롬프트 템플릿 + LLM 연결) ===")

# 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 Python 강사야. 한국어로 간결하게 설명해."),
    ("human", "{topic}이 뭐야? 세 줄로 설명해줘.")
])

# 프롬프트 + LLM 연결 (이게 Chain)
chain = prompt | llm

# 실행
result = chain.invoke({"topic": "Flask"})
print(result.content)

print()
result = chain.invoke({"topic": "RAG"})
print(result.content)



