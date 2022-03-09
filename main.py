import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.backend.api.api import router
from app.backend.api.dependencies import aio_http_client
from app.backend.settings import settings
from app.database.init_sql_script import start_phantom_migrations

application = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    openapi_url='/openapi.json',
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

application.include_router(router)


@application.on_event("startup")
async def startup():
    aio_http_client.start()

if __name__ == '__main__':
    start_phantom_migrations()
    uvicorn.run(
        'main:application',
        host=str(settings.HOST),
        port=settings.PORT,
        workers=settings.WORKERS,
        debug=settings.DEBUG
    )
