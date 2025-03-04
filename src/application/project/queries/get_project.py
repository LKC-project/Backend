from typing import Sequence

from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.project.dto import ProjectResponseDTO
from src.application.project.interfaces import ProjectReader


class GetProject(DTO, Query[Sequence[ProjectResponseDTO]]):
    id: int
    user_id: int


class GetProjectsByUserIDHandler(QueryHandler[GetProject, Sequence[ProjectResponseDTO]]):
    def __init__(self, reader: ProjectReader):
        self.reader = reader

    async def __call__(self, command: GetProject) -> ProjectResponseDTO:
        project = await self.reader.select_all_by_user_id(id=command.id, user_id=command.user_id)
