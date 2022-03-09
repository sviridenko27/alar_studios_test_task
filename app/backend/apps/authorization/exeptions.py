from fastapi import HTTPException
from starlette import status


class AuthorizeException:
    """
    Object with general exceptions for auth methods.
    """

    base = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authenticate error",
        headers={"WWW-Authenticate": "Bearer"},
    )

    incorrect_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_not_found = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_not_provided = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="User wasn't provided",
        headers={"WWW-Authenticate": "Bearer"},
    )
