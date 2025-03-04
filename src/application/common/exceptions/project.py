from fastapi import status

from src.application.common.exceptions.base import AuthError


class ProjectAccessDenied(AuthError):
    code = status.HTTP_403_FORBIDDEN
    detail = "You do not have access to this project"
