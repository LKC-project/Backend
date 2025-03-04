from typing import Protocol

from src.application.project.dto import ProjectDTO
from src.application.project.dto import UploadProjectDTO, UpdateProjectDTO


class ProjectRepo(Protocol):
    async def insert_one(self, user_id: int, project: UploadProjectDTO) -> ProjectDTO:
        raise NotImplementedError

    async def update_one(self, id: int, user_id: int, project: UpdateProjectDTO):  # TODO: Thint abou this
        raise NotImplementedError
