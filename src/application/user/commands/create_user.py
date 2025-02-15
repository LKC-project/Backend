from didiator import Command, CommandHandler

from src.application.user.dto import UserDTO, UserCreateDTO
from src.application.common.interfaces.uow import UnitOfWork
from src.infrastructure.db.repositories.user import UserRepoImpl


class UserCreate(UserCreateDTO, Command[UserDTO]):
    pass


class UserCreateHandler(CommandHandler[UserCreate, UserDTO]):
    def __init__(self, repo: UserRepoImpl, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    async def __call__(self, command: UserCreate) -> UserDTO:
        result = await self.repo.insert_one(command)
        await self.uow.commit()

        return result
