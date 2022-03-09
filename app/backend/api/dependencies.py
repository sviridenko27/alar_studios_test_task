import aiohttp as aiohttp
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlmodel import Session

from app.backend.apps.authorization.exeptions import AuthorizeException
from app.backend.apps.users.models import User
from app.backend.settings import settings
from app.database.connections import engine

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_session() -> Session:
    """
    Getting session with main database.
    """
    with Session(engine, expire_on_commit=False) as new_session:
        yield new_session


async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> User:
    """
    Getting authorized user as SQLModel User object.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise AuthorizeException.user_not_provided
    except JWTError:
        raise AuthorizeException.base

    user = User.get_user_by_name(username, session)
    if user is None:
        raise AuthorizeException.user_not_found

    return user


class AioHttpClient:
    session: aiohttp.ClientSession = None

    def start(self):
        self.session = aiohttp.ClientSession()

    async def stop(self):
        await self.session.close()
        self.session = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.session is not None
        return self.session


aio_http_client = AioHttpClient()
