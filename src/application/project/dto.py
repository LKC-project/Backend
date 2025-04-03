from pydantic import Field

from src.application.common.dto import DTO


class ProjectDTO(DTO):
    id: int
    name: str = Field(max_length=255)
    description: str | None = Field(default=None, max_length=512)
    content: dict | list | None = Field(default=None)


class UploadProjectDTO(DTO):
    name: str = Field(max_length=255)
    description: str | None = Field(default=None, max_length=512)
    content: dict | list | None = Field(default=None)


class UpdateProjectDTO(DTO):
    name: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=512)
    content: dict | list | None = Field(default=None)
