from fastapi import HTTPException
from starlette import status


class UserException:
    """
    Object with general exceptions for Users methods.
    """

    def __init__(self):
        pass

    already_exist = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='User already exist',
    )

    not_found = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='User not found'
    )

    not_enough_permissions = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='User have not enough permissions'
    )
