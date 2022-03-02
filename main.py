import uvicorn
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from app.backend.api.api import router
from app.backend.logger import Loggers
from app.backend.settings import settings

application = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
)

application.include_router(router, prefix=settings.API_V1_STR)

loggers = Loggers()

if __name__ == '__main__':
    uvicorn.run(
        'main:application',
        host=str(settings.HOST),
        port=settings.PORT,
        workers=settings.WORKERS,
        debug=settings.DEBUG
    )
