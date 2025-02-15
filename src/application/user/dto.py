from pydantic import Field

from src.application.common.dto import DTO


class UserDTO(DTO):
    id: int
    name: str = Field(max_length=48)
    avatar_url: str | None = Field(None, max_length=256)


class UserWithPasswordDTO(DTO):
    id: int
    name: str = Field(max_length=48)
    avatar_url: str | None = Field(None, max_length=256)
    password: str = Field(max_length=128)


class UserCreateDTO(DTO):
    name: str = Field(max_length=48)
    password: str = Field(max_length=128)
