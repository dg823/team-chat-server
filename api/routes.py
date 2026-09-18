# 백엔드 개발자 담당 영역
from fastapi import APIRouter
from pydantic import BaseModel
try:
    from core.llm import get_res
except:
    from ..core.llm import get_res

router = APIRouter()

class ChatReq(BaseModel):
    message: str
    history: list = []

@router.post("/chat")
def chat_endpoint(req: ChatReq):
    return {"res": get_res(req.message, req.history)}
