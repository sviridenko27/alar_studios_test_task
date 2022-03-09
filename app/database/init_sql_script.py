from app.backend.api.dependencies import get_session


def start_phantom_migrations():
    """
    Migrations like module for demonstrate some SQL code.

    P.S. Я честно говоря не знаю где в тестовом показать, что я знаю SQL, пусть хотя бы так будет.
    """
    session = next(get_session())
    session.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
          id bigserial primary key,
          username varchar(45) UNIQUE NOT NULL,
          password varchar(450) NOT NULL,
          is_admin boolean NOT NULL DEFAULT FALSE
        );
        
        INSERT INTO "user" 
        (
            username, 
            password,
            is_admin
        ) 
        values 
        (
            'admin',
            '$2b$12$6/odbH2uFT0I6.4AD9jRlekidwdl5na.rtxJyWptRoPBCHp8LCOSW', -- admin
            True
        )
        ON CONFLICT DO NOTHING
    """)
    session.commit()
