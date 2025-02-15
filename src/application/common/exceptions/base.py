from fastapi import status

from src.domain.common.exceptions.base import BaseAppError


class AppError(BaseAppError):
    pass


class AuthError(AppError):
    code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"


class UnexpectedError(AppError):
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Unexpected error"
