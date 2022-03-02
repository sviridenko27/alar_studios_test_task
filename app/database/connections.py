from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.backend.settings import settings

Base = declarative_base()

base_engine = create_engine(
    settings.MAIN_DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_POOL_SIZE_MAX_OVERFLOW
)

SessionLocal = sessionmaker(
    expire_on_commit=False,
    binds={
        Base: base_engine,
    }
)
