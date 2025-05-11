from pydantic import Field

from src.application.common.dto import DTO


class ImageDTO(DTO):
    url: str


class UploadImageDTO(DTO):
    name: str | None = Field(None, max_length=255)
    content: bytes


class UploadImageFromGoogleDriveDTO(DTO):
    file_id: str = Field(None, max_length=255)
    access_token: str
