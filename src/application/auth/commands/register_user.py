from didiator import Command, CommandHandler

from src.application.auth.dto import RegisterUserDTO, InsertUserDTO
from src.application.auth.interfaces import AuthRepo
from src.application.auth.password import Password
from src.infrastructure.db.uow import UnitOfWork


class RegisterUser(RegisterUserDTO, Command[None]):
    pass


class RegisterUserHandler(CommandHandler[RegisterUser, None]):
    def __init__(self, repo: AuthRepo, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    async def __call__(self, command: RegisterUser) -> None:
        user = InsertUserDTO(
            **command.model_dump(exclude={"password"}),
            hashed_password=Password.encode(command.password)
        )

        await self.repo.insert_one(user)
        await self.uow.commit()
