from typing import Protocol, Sequence

from src.application.auth.dto import UserDTO


class AuthReader(Protocol):
    async def select_by_id(self, id: int) -> UserDTO | None:
        raise NotImplementedError

    async def select_by_name(self, name: str) -> UserDTO | None:
        raise NotImplementedError

    async def select_by_email(self, email: str) -> UserDTO | None:
        raise NotImplementedError
