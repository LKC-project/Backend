from typing import Protocol

from src.application.user.dto import UserDTO, UserCreateDTO


class UserRepo(Protocol):

    async def insert_one(self, user: UserCreateDTO) -> UserDTO:
        raise NotImplementedError
