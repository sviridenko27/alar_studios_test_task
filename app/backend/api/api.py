from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.backend.api.dependencies import get_session
from app.backend.apps.authorization.models import Token
from app.backend.apps.authorization.utils import create_access_token, authenticate_user
from app.backend.settings import settings

router = APIRouter()


@router.post("/token", response_model=Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_session)
):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
