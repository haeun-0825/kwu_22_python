from typing import Literal
from pydantic import BaseModel, UUID4
from datetime import datetime

class ChatDTO(BaseModel):
    type: Literal["text", "voice"]      # 텍스트 or 음성
    query: str                          # 사용자 질문
    voice_path: str                     # 음성 파일 경로
    session_id: UUID4 | None = None     # 채팅 세션 번호(방 번호)
