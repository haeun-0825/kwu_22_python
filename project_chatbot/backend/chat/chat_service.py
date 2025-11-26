import openai
from chat.chat_llm import ChatLLM


class ChatService:
    
    def __init__(self):
        pass
    
    # 사용자로부터 질문(Query)를 받아 답변(Answer)을 생성하고 전달하는 기능
    async def gen_answer(self, query: str) -> str:
        
        # 답변 생성
        chat_llm = ChatLLM()
        answer = chat_llm.multiturn_chat(query)
        
        return answer