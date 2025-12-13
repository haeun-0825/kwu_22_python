from chat.chat_llm import ChatLLM
from chat.chat_schema import ChatDTO
from uuid import UUID
from sqlalchemy.orm import Session
from chat.chat_crud import ChatCRUD


class ChatService:
    
    def __init__(self):
        self.chat_crud = ChatCRUD()
    
    async def gen_answer(self, chat_dto: ChatDTO, session_id: UUID, llm: ChatLLM, db: Session) -> str:
        # Human Query를 DB에 저장
        chat = {
            "session_id": str(session_id),
            "msg_type": "Human",
            "message": chat_dto.query,
        }        
        self.chat_crud.save_chat(chat, db)

        # AI Answer 생성
        answer = llm.multiturn_chat(chat_dto.query, session_id)
        
        # AI Answer를 DB에 저장
        chat = {
            "session_id": str(session_id),
            "msg_type": "AI",
            "message": answer,
        }        
        self.chat_crud.save_chat(chat, db)
        
        return answer