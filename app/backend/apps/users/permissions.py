from functools import wraps

from app.backend.apps.users.exeptions import UserException


def is_admin_permission(func):
    """
    Checking current_user admin role.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        current_user = kwargs.get('current_user')

        if not current_user:
            raise UserException.not_found

        if not current_user.is_admin:
            raise UserException.not_enough_permissions

        return await func(*args, **kwargs)
    return wrapper
