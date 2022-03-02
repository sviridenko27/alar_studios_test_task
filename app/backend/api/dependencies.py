from sqlalchemy.orm import Session

from app.database.connections import SessionLocal


def get_session() -> Session:
    """
    Зависимость для получения новой сессии
    """
    with SessionLocal() as new_session:
        yield new_session
