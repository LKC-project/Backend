from src.application.common.exceptions.base import AuthError


class WrongLoginOrPassword(AuthError):
    detail = "Wrong login or password"


class InvalidToken(AuthError):
    pass


class Unauthorized(AuthError):
    pass
