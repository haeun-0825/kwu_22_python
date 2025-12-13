import os
from uuid import UUID
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


class ChatLLM:
    def __init__(self):
        _ = load_dotenv(find_dotenv())
        
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.2,
        )
        self._store = {}
        
        self.system_prompt = """
            너는 광주여자대학교 파이썬 수업의 'AI 조교'야. 
            학생의 질문에 대해 반드시 아래 제공된 <context> 내의 교수님 강의 자료를 바탕으로만 답변해야 해.

            [답변 규칙]
            1. 일반적인 상식보다 <context>에 있는 설명을 1순위로 사용해. 
            2. 교수님이 코드에 적어두신 유머나 강조 사항(예: "시험문제 내기 딱 좋다", "외우셔야 합니다")을 인용하면 아주 좋아.
            4. 만약 <context>에 없는 내용을 답해야 한다면 "우리 수업 자료에는 없지만 일반적인 파이썬 지식으로는~"이라고 먼저 말해줘.
            """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{query}"),
        ])

        base_chain = prompt | self.llm

        self.chain = RunnableWithMessageHistory(
            base_chain,
            get_session_history=self.get_history,
            input_messages_key="query",
            history_messages_key="history"
        )
        # 1. 강의 자료 로드 및 벡터 DB 생성 (서버 시작 시 1회 실행)
        # loader_args를 사용하여 TextLoader가 utf-8 인코딩으로 파일을 읽도록 설정합니다.
        # 'loader_args'를 'loader_kwargs'로 변경합니다.
        loader = DirectoryLoader(
            "./lecture", 
            glob="*.py", 
            loader_cls=TextLoader, 
            loader_kwargs={'encoding': 'utf-8'} # 이 부분을 수정하세요
        )
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50) # 코드는 조금 더 크게 자르는게 좋습니다.
        chunks = splitter.split_documents(docs)
        
        embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        vector_db = Chroma.from_documents(chunks, embeddings)
        self.retriever = vector_db.as_retriever(search_kwargs={"k": 3}) # 관련 내용 3개 검색

        # 2. 프롬프트에 context 변수 추가
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt), # 위에서 수정한 RAG용 시스템 프롬프트
            MessagesPlaceholder(variable_name="history"),
            ("human", "강의 내용을 바탕으로 질문에 답해줘.\n\n<context>\n{context}\n</context>\n\n질문: {query}"),
        ])
        
    
    def get_history(self, session_id: str) -> ChatMessageHistory:
        if session_id not in self._store:
            self._store[session_id] = ChatMessageHistory()
        return self._store[session_id]

    def multiturn_chat(self, query: str, session_id: UUID) -> str:
        # 1. 강의 자료에서 관련 내용 검색
        docs = self.retriever.invoke(query)
        
        # 2. 검색된 문서와 파일명을 매칭하여 context 생성
        context_list = []
        for d in docs:
            # 파일 경로에서 파일명만 추출 (예: lecture/04_collection.py -> 04_collection.py)
            file_path = d.metadata.get('source', '강의자료')
            file_name = os.path.basename(file_path) 
            context_list.append(f"[{file_name} 내용]:\n{d.page_content}")
        
        context = "\n\n".join(context_list)
        
        # 3. 답변 생성 시 context 전달
        result = self.chain.invoke(
            {
                "query": query, 
                "context": context 
            },
            config={"configurable": {"session_id": str(session_id)}},
        )
        return result.content
    