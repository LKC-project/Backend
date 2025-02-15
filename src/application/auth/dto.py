from pydantic import Field

from src.application.common.dto import DTO


class UserLoginDTO(DTO):
    name: str = Field(max_length=48)
    password: str = Field(max_length=128)
