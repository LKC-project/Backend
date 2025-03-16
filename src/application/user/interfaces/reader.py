from typing import Protocol, Sequence

from src.application.user.dto import UserDTO


class Filters:
    ...


class UserReader(Protocol):
    async def select_by_id(self, id: int) -> UserDTO | None:
        raise NotImplementedError

    async def select_by_name(self, name: str) -> UserDTO | None:
        raise NotImplementedError

    async def select_all(self, filters: Filters, pagination: ...) -> Sequence[UserDTO]:
        raise NotImplementedError
