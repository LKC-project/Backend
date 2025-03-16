from pydantic import Field, EmailStr

from src.application.common.dto import DTO


class UserDTO(DTO):
    id: int
    name: str = Field(max_length=48)
    email: EmailStr
    avatar_url: str | None = Field(None, max_length=256)
    active: bool
