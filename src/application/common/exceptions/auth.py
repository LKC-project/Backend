from fastapi import status

from src.application.common.exceptions.base import AuthError


class EmailAlreadyInUse(AuthError):
    code = status.HTTP_409_CONFLICT
    detail = "This email is already in use"


class WrongEmailOrPassword(AuthError):
    detail = "Wrong email or password"


class InvalidToken(AuthError):
    pass


class Unauthorized(AuthError):
    pass


class GoogleAuthorizationError(AuthError):
    detail = "Authorization error, try again later"
