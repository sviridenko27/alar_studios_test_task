from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.backend.api.dependencies import get_session, get_current_user
from app.backend.apps.users.exeptions import UserException
from app.backend.apps.users.models import User, UserRequestModel, UserResponseModel
from app.backend.apps.users.permissions import is_admin_permission

router = APIRouter(prefix='/users')


@router.get('', summary='Get users', response_model=List[UserResponseModel])
async def users_list(
        session: Session = Depends(get_session),
        _: User = Depends(get_current_user),
):
    """
    [Get] system users list with base info.
    """
    return session.exec(select(User)).all()


@router.post('', summary='Create user', response_model=UserResponseModel)
@is_admin_permission
async def create(
        user: UserRequestModel,
        session: Session = Depends(get_session),
        current_user: User = Depends(get_current_user),
):
    """
    [Create] system user.
    """
    is_user_exist = User.get_user_by_name(user.username, session)
    if is_user_exist:
        raise UserException.already_exist

    user = User.validate(user)
    session.add(user)
    session.commit()

    return user


@router.delete('/{user_id}', summary='Delete user')
@is_admin_permission
async def delete_user(
        user_id: int,
        session: Session = Depends(get_session),
        current_user: User = Depends(get_current_user),
):
    """
    [Delete] system user by id.
    """
    user = session.get(User, user_id)
    if not user:
        raise UserException.not_found

    session.delete(user)
    session.commit()

    return {'ok': True}


@router.patch('/{user_id}', summary='Update user', response_model=UserResponseModel)
@is_admin_permission
async def update_user(
        user_id: int,
        updated_user: UserRequestModel,
        session: Session = Depends(get_session),
        current_user: User = Depends(get_current_user)
):
    """
    [Update] system user by id.
    """
    user = session.get(User, user_id)
    if not user:
        raise UserException.not_found

    user_data = updated_user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)

    return user
