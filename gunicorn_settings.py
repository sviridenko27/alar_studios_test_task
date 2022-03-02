import multiprocessing

from app.backend.settings import settings

bind = f'{settings.HOST}:{settings.PORT}'
workers = settings.WORKERS or multiprocessing.cpu_count() * 2 + 1
worker_class = 'uvicorn.workers.UvicornWorker'
