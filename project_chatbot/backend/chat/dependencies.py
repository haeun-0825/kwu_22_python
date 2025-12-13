from functools import lru_cache
from chat.chat_llm import ChatLLM

@lru_cache()
def get_chat_llm() -> ChatLLM:
    return ChatLLM()