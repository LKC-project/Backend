from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.domain.common.exceptions.base import BaseAppError


class AppErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except BaseAppError as exception:
            return JSONResponse(
                content={"detail": exception.detail},
                status_code=exception.code,
            )

