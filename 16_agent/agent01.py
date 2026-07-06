from langchain_groq import ChatGroq
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent  # 새 방식
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

@tool
def calculator(expression: str) -> str:
    """수학 계산을 수행합니다. 예: '15 * 3', '100 + 50'"""
    try:
        return str(eval(expression))
    except:
        return "계산할 수 없습니다."

@tool
def search_company_rules(query: str) -> str:
    """회사 규정(연차, 급여, 복지, 재택근무)에 관한 질문에 답합니다."""
    client = chromadb.PersistentClient(
        path=os.path.join(os.path.dirname(__file__), "..", "15_chromadb", "chroma_db")
    )
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    collection = client.get_or_create_collection("company_rules", embedding_function=embedding_fn)
    results = collection.query(query_texts=[query], n_results=2)
    return "\n".join(results["documents"][0])

tools = [calculator, search_company_rules]

# LangChain 1.x 이상 → LangGraph 방식으로 Agent 생성
agent = create_react_agent(
    llm,
    tools,
    prompt="한국어로만 답해. 질문에 맞는 도구를 선택해서 사용해."
)

questions = [
    "연차가 며칠이야?",
    "15 곱하기 3은?",
    "재택근무 며칠 가능하고, 그게 일주일 5일 중 몇 퍼센트야?"
]

for q in questions:
    print(f"\n{'='*50}")
    print(f"질문: {q}")
    result = agent.invoke({
        "messages": [{"role": "user", "content": q}]
    })
    # messages 리스트의 마지막 메시지가 최종 답변
    print(f"최종 답변: {result['messages'][-1].content}")
