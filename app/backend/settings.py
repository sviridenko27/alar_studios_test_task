import os
from typing import Optional, Union, List

from pydantic import BaseSettings, PostgresDsn, AnyUrl, IPvAnyAddress, AnyHttpUrl


class Settings(BaseSettings):
    """
    Service configuration.
    """

    DEBUG: bool = False

    # service description
    APP_VERSION: str = '1.0.0'
    APP_TITLE: str = 'Storage'
    APP_DESCRIPTION: str = 'Alar test task'

    # server settings
    PORT: int = 5002
    HOST: Union[IPvAnyAddress, AnyUrl] = '0.0.0.0'
    WORKERS: Optional[int]

    # database settings
    MAIN_DATABASE_URL: PostgresDsn
    DATABASE_POOL_SIZE: int = 1
    DATABASE_POOL_SIZE_MAX_OVERFLOW: int = 3

    # authorization settings
    SECRET_KEY: str = "TEST"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # business logic settings
    REMOTE_SERVICES_URLS: List[AnyHttpUrl]
    REQUEST_TIMEOUT_SECONDS: int = 120


settings = Settings(_env_file='.environment' if os.path.exists('.environment') else '.environment.example')
