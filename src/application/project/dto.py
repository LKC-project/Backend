from pydantic import Field

from src.application.common.dto import DTO


class ProjectDTO(DTO):
    id: int
    name: str = Field(max_length=255)
    description: str | None = Field(default=None, max_length=512)


class ProjectResponseDTO(ProjectDTO):
    url: str


class UploadProjectDTO(DTO):
    name: str | None = Field(None, max_length=255)
    description: str | None = Field(default=None, max_length=512)


class UpdateProjectRequestDTO(DTO):
    name: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=512)
    content: dict | None = Field(default=None)


class UpdateProjectDTO(DTO):
    name: str | None = Field(default=None, max_length=255)
    description: str | None = Field(default=None, max_length=512)
