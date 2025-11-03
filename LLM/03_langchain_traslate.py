import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

llm = ChatOpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    model="gpt-4.1-mini",
    temperature=0.5
)

system_prompt = """
    너는 영어권 학생들을 대상으로 하는 강의자료를 만드는 보조야.
    내가 전달하는 한국어 문장을 조건에 맞게 영어로 번역해줘.
    
    조건1. 질문에 대해 답변하지 마세요. 번역만 하세요.
    조건2. 전달한 문장을 대학교 강의에 맞게 번역해주세요.
    조건3. 문법에 신경써서 번역해주세요.
    조건4. 줄임말과 신조어 등은 최대한 사용하지 마세요.
"""

prompts = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{query}")
])

chain = prompts | llm

query= input("한글: ")

result = chain.invoke({"query": query})
print(f"영문: {result.content}")