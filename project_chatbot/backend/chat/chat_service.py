import openai
from chat.chat_llm import ChatLLM
from uuid import UUID


class ChatService:
    
    def __init__(self):
        pass
    
    # 사용자로부터 질문(Query)를 받아 답변(Answer)을 생성하고 전달하는 기능
    async def gen_answer(self, query: str, session_id: UUID, llm: ChatLLM) -> str:
        
        # 답변 생성
        answer = llm.multiturn_chat(query, session_id)
        
        return answer


class ChatService:
    
    def __init__(self):
        pass
    
    # 사용자로부터 질문(Query)를 받아 답변(Answer)을 생성하고 전달하는 기능
    async def gen_answer(self, query: str, session_id: UUID, llm: ChatLLM) -> str:
        
        # 답변 생성
        answer = llm.multiturn_chat(query, session_id)
        
        return answer