from pydantic import BaseModel, Field


class SUserAdd(BaseModel):
    name: str = Field(max_length=48)
    hashed_password: bytes = Field(max_length=60)


class SUser(BaseModel):
    id: int
    name: str = Field(max_length=48)
    avatar_url: str = Field(max_length=256)


class SUserFull(BaseModel):
    id: int
    name: str = Field(max_length=48)
    avatar_url: str = Field(max_length=256)
    hashed_password: bytes = Field(max_length=60)


class SUserEdit(BaseModel):
    name: str | None = Field(None, max_length=48)
    avatar_url: str | None = Field(None, max_length=256)
    hashed_password: bytes | None = Field(None, max_length=60)
