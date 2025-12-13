import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import chat_router

app = FastAPI()  # FastAPI를 사용해서 Backend 서버 구축

origins = [
    "http://localhost:5500"  # 프론트엔드 도메인 주소
]

# CORS(Cross Origin Resource Sharing)
#  - 브라우저가 다른 도메인 간 요청을 보안 때문에 제한하는 정책
#  - 프론트엔드 → 백엔드 요청을 보내면 기본적으로 브라우저가 막음(보안 이슈)
#  - 특정 도메인은 허용해주세요~ → CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중이면 *, 배포 시 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router.router)

# Backend 서버 구동!
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=9000)