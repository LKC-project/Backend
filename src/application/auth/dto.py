from pydantic import Field

from src.application.common.dto import DTO


class UserDTO(DTO):
    id: int
    name: str = Field(max_length=48)
    hashed_password: bytes = Field(max_length=60)


class InsertUserDTO(DTO):
    name: str = Field(max_length=48)
    hashed_password: bytes = Field(max_length=60)


class LoginUserDTO(DTO):
    name: str = Field(max_length=48)
    password: str = Field(max_length=128)


class RegisterUserDTO(DTO):
    name: str = Field(max_length=48)
    password: str = Field(max_length=128)
