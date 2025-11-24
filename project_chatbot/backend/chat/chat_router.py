from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from chat.chat_schema import ChatDTO
from chat.chat_service import ChatService

# 127.0.0.1:9000 → 도메인주소

router = APIRouter(prefix="/api")

# 127.0.0.1:9000/api/chat
@router.post("/chat")
async def chat(chat_dto: ChatDTO):
    query = chat_dto.query.strip()
    print(f"Human: {query}")
    
    chat_service = ChatService()
    answer = await chat_service.gen_answer(query)
    
    print(f"AI: {answer}")
    
    return{"success_code": 200, "answer": answer}
