from fastapi import status

from src.application.common.exceptions.base import AuthError


class UsernameAlreadyInUse(AuthError):
    code = status.HTTP_409_CONFLICT
    detail = "This username is already in use"


class WrongLoginOrPassword(AuthError):
    detail = "Wrong login or password"


class InvalidToken(AuthError):
    pass


class Unauthorized(AuthError):
    pass
