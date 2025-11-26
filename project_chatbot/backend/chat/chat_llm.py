import os
import uuid
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

class ChatLLM:
    def __init__(self):
        _ = load_dotenv(find_dotenv())
        
        llm = ChatOpenAI(
            model = "gpt-4.1-mini", 
            api_key = os.getenv("OPENAI_API_KEY"), 
            temperature = 0.2, 
        )  
        session_id = str(uuid.uuid4())
        _store = {}
        
        system_prompt = """
            너는 사용자의 질문에 도움을 주는 어시스턴트야.
            사용자의 질문에 대한 답변을 생성해줘.
        """
        
    
    def multiturn_chat(self, query: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),                        
            MessagesPlaceholder(variable_name="history"),       
            ("human", "{query}"),                              
        ])

        base_chain = prompt | self.llm

        chain = RunnableWithMessageHistory(
            base_chain,
            get_session_history = self.get_history,
            input_messages_key = "query",
            history_messages_key = "history"
        )

        result = chain.invoke(
            {"query": query},
            config={"configurable": {"session_id": self.session_id}},
        )
        
        return result.content
    
    def get_history(self, session_id: str) -> ChatMessageHistory:
        if session_id not in self._store:
          self._store[session_id] = ChatMessageHistory()
        return self._store[session_id]