from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.domain.common.exceptions.base import BaseAppError

from src.presentation.api.exceptions import ExceptionResponse


class AppErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except BaseAppError as exception:
            return JSONResponse(
                content=ExceptionResponse(detail=exception.detail).model_dump(),
                status_code=exception.code,
            )

