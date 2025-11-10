# Langchain
#  - Python 언어 기반의LLM을 쉽게 사용할 수 있게 도와주는 라이브러리
#  - 챗봇, 에이전트 등을 개발

# * GPT API를 사용해서도 챗봇 또는 에이전트 개발 가능
# * Gemini API를 사용해서도 챗봇 또는 에이전트 개발 가능
# * Cluade API
# * Grok API, ...
# 왜? Langchain? 그냥 GPT API를 사용하면 되는 거 아닌가..
#  - 현재 LLM은 춘추전국시대
#  - 만약에 GPT API 개발 + Gemini API로 변경 (전체 코드 수정해야 됨)
#  - Langchain을 사용 -> 모델 변경 (코드 1줄만 수정하면 됨)

import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. env 불러오기 (API-KEY)
_= load_dotenv(find_dotenv())

# 2. LLM 모델
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0, # 1에 가까울수록 AI 창의력 ↑ (0~1 범위)
)

# 3. 프롬프트
#  - LLM으로부터 원하는 답변을 얻기 위한 명령
#  - 3가지 프롬프트
#   가. System prompt: 역할, 설정, 명령 하는 것
#   나. Human Prompt: 질문(Query)
#   다. AI Prompt: 답변(AI가 생성한)
system_prompt = """
    너는 사용자의 질문에 도움을 주는 어시스턴트야.
    사용자의 질문에 대한 답변을 생성해줘.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{query}")
])

# 4. Chain 생성
chain = prompt | llm

# 5. Chain 실행
query = "나의 이름은 전하은이야"
answer = chain.invoke({"query": query})
print(answer)

# Langchain 챗봇
# 1. api-key 불러오기
# 2. LLM 모델
# 3. Prompt 작성
# 4. Chain 생성
# 5. 실행

# 싱글턴 챗봇: 질문 -> 답변 끝 (대화X)
#  ㄴ System + Human
# 멀티턴 챗봇: 대화(질문, 답변, 질문, 답변 저장)
#  ㄴ System + History + Human
