from chat.chat_model import ChatHistory
from datetime import datetime
from sqlalchemy.orm import Session

class ChatCRUD:
    def __init__(self):
        pass
    

    def save_chat(self, chat: dict, db: Session):
        chat_history = ChatHistory(
            session_id=chat["session_id"],
            msg_type=chat["msg_type"],
            message=chat["message"],
            regdate=datetime.now()
        )
        
        db.add(chat_history)
        db.commit()