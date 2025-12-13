from functools import lru_cache
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.config import get_settings

@lru_cache()
def get_engine():
    settings = get_settings()
    return create_engine(
        settings.DB_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        future=True,
    )

SessionLocal = sessionmaker(
    bind=get_engine(), 
    autocommit=False, 
    autoflush=False,
    expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()