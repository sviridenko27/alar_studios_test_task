from fastapi import APIRouter

from .endpoints.authorizations import router as auth_router
from .endpoints.remote_services import router as remote_services_router
from .endpoints.users import router as user_router

router = APIRouter()
router.include_router(auth_router, tags=['auth'])
router.include_router(user_router, tags=['user'])
router.include_router(remote_services_router, tags=['remote'])
