from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    session_id = Column(String, primary_key=True, index=True)
    msg_type = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    regdate = Column(DateTime, nullable=False)
    
    def __init__(self, session_id, msg_type, message, regdate):
        self.session_id = session_id
        self.msg_type = msg_type
        self.message = message
        self.regdate = regdate
        
    def __repr__(self):
        return f"<ChatHistory({self.session_id}, {self.msg_type}, {self.message}, {self.regdate})>"