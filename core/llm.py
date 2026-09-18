# AI 엔지니어 담당 영역
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
try:
    from config import KEY, MODEL # 직접 실행 시
except:
    from ..config import KEY, MODEL # 패키지로 실행 시

llm = ChatGroq(temperature=0.7, model_name=MODEL, groq_api_key=KEY)

def get_res(msg: str, hist: list):
    try:
        msgs = [SystemMessage(content="You are a helpful assistant.")]
        for h in hist:
            if h["role"] == "user": msgs.append(HumanMessage(content=h["content"]))
            elif h["role"] == "assistant": msgs.append(AIMessage(content=h["content"]))
        msgs.append(HumanMessage(content=msg))
        return llm.invoke(msgs).content
    except Exception as e:
        return f"Core Error: {str(e)}"
