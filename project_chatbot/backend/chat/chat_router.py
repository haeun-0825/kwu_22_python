from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from chat.chat_schema import ChatDTO
from chat.chat_service import ChatService
from chat.chat_llm import ChatLLM
from chat.dependencies import get_chat_llm

# 127.0.0.1:9000 → 도메인주소

router = APIRouter(prefix="/api")

# 127.0.0.1:9000/api/chat
@router.post("/chat")
async def chat(chat_dto: ChatDTO, llm: ChatLLM = Depends(get_chat_llm)):
    query = chat_dto.query.strip()
    print(f"Human: {query}")
    
    session_id = chat_dto.session_id
    print(f"SessionID: {session_id}")
    
    chat_service = ChatService()
    answer = await chat_service.gen_answer(query, session_id, llm)
    
    print(f"AI: {answer}")
    
    return{"success_code": 200, "answer": answer}
