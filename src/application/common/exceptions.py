from fastapi import status

from src.domain.common.exceptions.base import BaseAppError


class AppError(BaseAppError):
    pass


class UnexpectedError(AppError):
    http_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Unexpected error"


class CommitError(UnexpectedError):
    pass


class RollbackError(UnexpectedError):
    pass
