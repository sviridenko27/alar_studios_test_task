from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.backend.api.dependencies import get_session
from app.backend.apps.authorization.models import Token, AuthForm
from app.backend.apps.users.models import User

router = APIRouter(prefix='/auth')


@router.post("/token", summary='Get user and authorization token', response_model=Token)
async def login(
        credentials: AuthForm,
        session: Session = Depends(get_session)
):
    """
    Main authorization method for getting auth bearer token [OAuth2].
    """
    return User.get_authenticate_user_token(credentials.username, credentials.password, session)
