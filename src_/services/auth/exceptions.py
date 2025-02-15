from fastapi import HTTPException as _HTTPException, status as _status


NotAuthenticatedException = _HTTPException(
    status_code=_status.HTTP_403_FORBIDDEN,
    detail="Not authenticated"
)
