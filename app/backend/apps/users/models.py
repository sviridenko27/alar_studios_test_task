from datetime import timedelta
from typing import Optional

from pydantic import validator
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Session, select

from app.backend.apps.authorization.exeptions import AuthorizeException
from app.backend.apps.authorization.models import Token
from app.backend.apps.authorization.utils import create_access_token, verify_password, is_hash, get_password_hash
from app.backend.settings import settings


class BaseUserInfo(SQLModel):
    username: str = Field(sa_column=Column("username", String, unique=True))
    is_admin: bool


class UserRequestModel(BaseUserInfo):
    password: str

    @validator('password')
    def hash_password(cls, value):
        if not value or is_hash(value):
            return value
        return get_password_hash(value)


class UserResponseModel(BaseUserInfo):
    id: Optional[int] = Field(default=None, primary_key=True, title='Идентификатор')


class User(UserResponseModel, UserRequestModel, table=True):

    @classmethod
    def get_user_by_name(cls, name: str, session: Session):
        return session.exec(select(User).where(User.username == name)).first()

    @staticmethod
    def get_authenticate_user_token(username: str, password: str, session: Session):
        user = User.get_user_by_name(username, session)
        if not user:
            raise AuthorizeException.user_not_found
        if not verify_password(password, user.password):
            raise AuthorizeException.incorrect_credentials

        access_token = create_access_token(
            data={"sub": user.username},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )

        return Token(access_token=access_token, token_type='bearer')
