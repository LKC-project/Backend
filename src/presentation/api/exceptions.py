from pydantic import BaseModel


class ExceptionResponse(BaseModel):
    detail: str


EXCEPTION_RESPONSE_MODEL = {
    "model": ExceptionResponse
}
