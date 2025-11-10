# input → LLM(GPT-4.1-mini) → answer

# > input 정의!
#   1. System Prompt(답변 생성 관련 명령)
#   2. Human Prompt(질의: Query)
#   3. chat history(사람-AI 대화 기록)

# > answer
#   1. ai prompt(답변 생성)

# 멀티턴 챗봇의 핵심: Chat History
#   ㄴ 1. Memory: 휘발성, 속도 ↑
#   ㄴ 2. Database: 영속성, 속도 ↓

import os
import uuid
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# 1. .env파일 불러오기
_ = load_dotenv(find_dotenv())

# 2. LLM 모델
llm = ChatOpenAI(
    model = "gpt-4.1-mini", 
    api_key = os.getenv("OPENAI_API_KEY"), 
    temperature = 0.2, 
)

# +. 세션별 히스토리 저장소(휘발성)
#   - 현재 대화기록(히스토리)은 메모리에 저장되기 때문에 서버가 종료되면 소멸됨
#       ㄴ 영구적으로 보관하고 싶은 경우 → 데이터베이스 사용!
#   - 세션 → 사용자의 대화 Room
#       ㄴ 예진 → 세션 A, 세션 B, 세션 C
#       ㄴ 고은 → 세션 D, 세션 E, 세션 F
#       ㄴ 하은 → 세션 S, 세션 Z, 세션 A  (세션이름은 중복 X)
#   - 중복되면 안되는 경우 → UUID(난수값) 값을 사용!
session_id = str(uuid.uuid4())

#   - 세션별 히스토리 저장소(휘발성)
_store = {}

def get_history(session_id: str) -> ChatMessageHistory:
    # session_id가 메모리에 없는 경우 생성 후 가져오기,
    #                      있는 경우 가져오기
    if session_id not in _store:
        _store[session_id] = ChatMessageHistory()
    return _store[session_id]

# 3. Prompt 작성
system_prompt = """
    너는 사용자의 질문에 도움을 주는 어시스턴트야.
    사용자의 질문에 대한 답변을 생성해줘.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),                         # System Prompt
    MessagesPlaceholder(variable_name="history"),       # Chat History
    ("human", "{query}"),                              # Human Prompt
])

# 4. Chain 생성
base_chain = prompt | llm

chain = RunnableWithMessageHistory(
    base_chain,
    get_session_history = get_history,
    input_messages_key = "query",
    history_messages_key = "history"
)

# 5. Chain 실행

while True:
    # 5.1 사용자로부터 질문 받기
    query = input("Human: ")
    if query.lower() == "exit":
        break
    
    # 5.2 AI에게 프롬프트 전달 및 답변 생성하기
    result = chain.invoke(
        {"query": query},
        config={"configurable": {"session_id": session_id}},
    )
    
    # 5.3 답변 출력하기
    print(f"AI: {result.content}")
    
    # 5.4 히스토리 출력
    history = get_history(session_id)
    print(f"히스토리 상태: {len(history.messages)}")
    
    