from functools import lru_cache

@lru_cache()
def get_engine():
    settings = get_settings()
    return create_engine(
        settings.database_url,
        pool_pre_pint=True,
        pllo_size=5,
        max_overflow=10,
        future=True,
    )
    
SessionLocal = sessionmaker(
    bind=get_engine(),
    autocommit=False(),
    autoflush=False,
    expire_on_commit=False
)