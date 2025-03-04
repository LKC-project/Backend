from typing import Protocol, Sequence

from src.application.project.dto import ProjectDTO


class ProjectReader(Protocol):
    async def select_all_by_user_id(self, id: int) -> Sequence[ProjectDTO]:
        raise NotImplementedError

    async def select_by_id(self, id: int) -> ProjectDTO | None:
        raise NotImplementedError

    async def select_all_by_id_and_user_id(self, id: int, user_id: int) -> ProjectDTO | None:
        raise NotImplementedError

