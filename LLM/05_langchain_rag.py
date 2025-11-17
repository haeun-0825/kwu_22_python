# RAG(검색 증강 생성)
#   - Retrieval Augmentaed Generation
#   - LLM 기본적으로 학습하는데 천문학적인 금액 소모
#       ㄴ LLM을 현재 학습했을 시점까지의 정보만 알고 있음
#       ㄴ 예를 들어, 2025년 05월 31일 학습을 한 모델의 경우
#          6월 1일부터의 정보는 없음!
#       문제점 1: 최신 데이터 반영 X
#       문제점 2: 할루시네이션(환각) → LLM 거짓말쟁이
#       → RAG

# ** RAG **
#   - Human(Query) → LLM(GPT) → Answer
#   - Human(Query) + 검색결과 → LLM(GPT) → Answer

# 예를 들어: 삼성전자 모바일 사업부 갤럭시 QnA 챗봇을 개발 임무
#   ㄴ 기존에 LLM은 갤럭시 스마트폰에 대한 자세한 정보 X
#   ㄴ 사용자가 갤럭시에 대한 질문을 하면 그냥 보편적인 답변만 생성
#   ㄴ 갤럭시 스마트폰에 대한 정보가 담긴 PDF파일 생성
#   ㄴ PDF파일로부터 사용자의 질문과 유사한 정보를 Retrieval(검색)
#   ㄴ 검색 된 정보를 사용자 질문과 함께 LLM에게 전달

# RAG 아키텍처
#   1. 지식 베이스
#        ㄴ 자료(PDF, PPT, Excel) → 불러오기(loader()) → Chunk 단위로 분할 
#           → Text Embedding → Vector DB에 저장

# * Text Embedding
#   - 단어 또는 문장을 1차원 숫자값의 나열로 변환 → 벡터
#   - [1, 5, 3, 2, 7] → 벡터
#   - 임베딩시 고려할 사항은 청크를 몇개의 숫자로 표현?
#       ㄴ 1521개의 숫자로 표현

# PDF → Chunk 1 → 벡터(5, 2, 12, ...) n=1521
#     → Chunk 2 → 벡터(1, 52, 3, ...) n=1521
#     → Chunk 3 → 벡터(99, 3, 4, ...) n=1521


import os
import pprint

from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.document_transformers import EmbeddingsRedundantFilter

_ = load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
    temperature=0.2
)

# RAG 프로세스
#   1. 지식 베이스 생성
#        ㄴ PDF파일 불러오기
pdf_path = "./LLM/data/agent.pdf"
docs = PyPDFLoader(pdf_path).load()  # PDF파일 불러옴
#        ㄴ 청크 단위로 분할하기
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
    )
chunks = splitter.split_documents(docs)
#        ㄴ 텍스트 임베딩 하기(벡터 변환: 1차원 숫자값 나열: 1521개 숫자)
embeddings = OpenAIEmbeddings(api_key=api_key)
#        ㄴ 벡터DB에 저장하기
vector_db = Chroma.from_documents(
    chunks, 
    embeddings, 
    collection_name="pdf-agent"
    )
retriever = vector_db.as_retriever()  # 검색기

# 벡터DB에서 검색된 결과 중 중복된 결과 제거 역할!
deduper = EmbeddingsRedundantFilter(embeddings=embeddings)


#   2. 지식 베이스 활용
#        ㄴ 사용자의 질문(Query)을 텍스트 임베딩 하기
#        ㄴ 벡터DB에서 사용자의 질문과 유사한 값 찾기 → 검색 결과
def retrieve_documents(query: str, k: int=3) -> str:
    # chunk 중 사용자 query와 가장 유사한 3개의 chunk만 활용!
    retriever.search_kwargs["k"] = k  # 몇 개의 chunk 사용할건지 설정
    docs = retriever.invoke(query)  # 검색 후 3개의 chunk 선별!
    docs = deduper.transform_documents(docs)  # 중복 된 내용 제거!
    return format_docs(docs)

# 검색 된 결과를 LLM에게 전달하기 전 읽기 쉽게 포맷을 변경
def format_docs(docs):
    out = []
    for i, d in enumerate(docs, 1):
        src = d.metadata.get("source", "unknown")
        out.append(f"[Doc {i}] (source: {src})\n{d.page_content}\n")
    return "\n".join(out)


#   3. 답변 생성
#        ㄴ 시스템 프롬프트
system_prompt= """
    아래에서 제공 된 Context만 사용해서 답변을 간결하고 정확하게 생성하세요.
    확실하지 않으면 "답변이 어렵습니다."라고 출력하세요.
    답변 끝에 참고한 [Doc #] 번호를 명시하세요 \n\n
    <context>\n{context}\n</context>\n\n
"""
#        ㄴ 휴먼 프롬프트(= 사용자 질문)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{query}")
])
#        ㄴ 검색 결과 
chain = {
    "context":RunnableLambda(lambda x: retrieve_documents(x["query"])),
    "query": RunnablePassthrough()  # Agent를 설명해줘
}| prompt | llm
#        ㄴ 를 LLM에게 전달하고 답변 생성
while True:
    query = input("Human: ").strip()
    if not query:
        continue
    elif query.lower() in {"exit", "quit"}:
        break
    
    # 답변 생성
    result = chain.invoke({"query": query})
    print("AI: ", result.content)
    
    # 답변 생성시 참고한 문서 확인
    context = retrieve_documents(query)
    print("=== RETRIEV CONTEXT ===")
    print(context)
    print("=== END ===")
