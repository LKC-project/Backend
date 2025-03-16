from pydantic import Field, EmailStr

from src.application.common.dto import DTO


class UserDTO(DTO):
    id: int
    name: str = Field(max_length=48)
    email: EmailStr
    hashed_password: bytes | None = Field(max_length=60)


class InsertUserDTO(DTO):
    name: str = Field(max_length=48)
    email: EmailStr
    avatar_url: str | None = Field(None, max_length=256)
    hashed_password: bytes | None = Field(max_length=60)


class LoginUserDTO(DTO):
    email: EmailStr
    password: str = Field(max_length=128)


class RegisterUserDTO(DTO):
    name: str = Field(max_length=48)
    email: EmailStr
    password: str = Field(max_length=128)


class GoogleAuthDTO(DTO):
    credential: str = Field(max_length=4096)
