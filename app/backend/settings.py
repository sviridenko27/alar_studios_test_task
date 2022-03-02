import multiprocessing
from typing import Optional, Union

from pydantic import BaseSettings, PostgresDsn, FilePath, AnyUrl, IPvAnyAddress


class Settings(BaseSettings):
    """
    Service configuration.
    """

    DEBUG: bool = False

    # service description
    APP_DESCRIPTION: str = ''
    APP_VERSION: str = '1.0.0'
    APP_TITLE: str = 'Хранилище'
    API_V1_STR: str = '/api/v1'

    # gunicorn settings
    PORT: int = 5002
    HOST: Union[IPvAnyAddress, AnyUrl] = '0.0.0.0'
    WORKERS: Optional[int]

    # database settings
    MAIN_DATABASE_URL: PostgresDsn
    DATABASE_POOL_SIZE: int = 1
    DATABASE_POOL_SIZE_MAX_OVERFLOW: int = 3

    # authorization settings
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = '.environment'


settings = Settings()
