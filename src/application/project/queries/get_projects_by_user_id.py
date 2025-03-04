from typing import Sequence

from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.project.dto import ProjectDTO
from src.application.project.interfaces import ProjectReader


class GetProjectsByUserID(DTO, Query[Sequence[ProjectDTO]]):
    user_id: int


class GetProjectsByUserIDHandler(QueryHandler[GetProjectsByUserID, Sequence[ProjectDTO]]):
    def __init__(self, reader: ProjectReader):
        self.reader = reader

    async def __call__(self, command: GetProjectsByUserID) -> Sequence[ProjectDTO]:
        return await self.reader.select_all_by_user_id(command.user_id)
