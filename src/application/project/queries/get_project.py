from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.project.dto import ProjectDTO
from src.application.project.interfaces import ProjectReader


class GetProjectByID(DTO, Query[ProjectDTO | None]):
    id: int


class GetProjectByIDHandler(QueryHandler[GetProjectByID, ProjectDTO | None]):
    def __init__(self, reader: ProjectReader):
        self.reader = reader

    async def __call__(self, command: GetProjectByID) -> ProjectDTO | None:
        return await self.reader.select_by_id(id=command.id)
