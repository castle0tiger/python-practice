# STEP 1 — Groq을 LangChain 방식으로 부르기
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path=os.path.join(SCRIPT_DIR, "..", ".env"))

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


# STEP 2 — 프롬프트 템플릿 (붕어빵 틀의 프롬프트 버전)
answer = llm.invoke("파이썬이 뭐야? 한 문장으로 답해. 한국어로만 답변을 구성해")
print(answer.content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 파이썬 강사야. 한국어로 두 문장 이내로 답해."),
    ("human", "{topic}이 뭐야?")
])

message = prompt.invoke({"topic": "리스트"})
answer = llm.invoke(message)
print(answer.content)


# STEP 3 — 파이프(|)로 연결하기 — 오늘의 하이라이트
chain = prompt | llm
answer = chain.invoke({"topic": "딕셔너리"})
print(answer.content)


#STEP 4 — 템플릿 재사용 (오늘의 결론)
topics = ["for문", "함수", "클래스"]

for t in topics:
    answer = chain.invoke({"topic": t})
    print(f"--- {t} ---")
    print(answer.content)
