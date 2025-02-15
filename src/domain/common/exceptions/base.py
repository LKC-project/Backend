class BaseAppError(Exception):
    code: int
    detail: str
