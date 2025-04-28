from typing import Protocol

from src.application.user.dto import UserDTO
from src.application.auth.dto import RegisterUserDTO


class UserRepo(Protocol):

    async def insert_one(self, user: RegisterUserDTO) -> UserDTO:
        raise NotImplementedError
