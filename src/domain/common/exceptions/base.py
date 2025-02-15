class BaseAppError(Exception):
    http_status_code: int | None
    status_code: int
    detail: str
