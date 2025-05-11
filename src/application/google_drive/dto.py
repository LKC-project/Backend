from src.application.common.dto import DTO


class UploadProjectDTO(DTO):
    access_token: str
    project: str


class UploadProjectResponseDTO(DTO):
    file_name: str
