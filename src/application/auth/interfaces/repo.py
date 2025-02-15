from typing import Protocol

from src.application.user.dto import UserDTO
from src.application.auth.dto import InsertUserDTO


class AuthRepo(Protocol):
    async def insert_one(self, user: InsertUserDTO) -> UserDTO:
        raise NotImplementedError
