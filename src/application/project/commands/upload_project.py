from didiator import Command, CommandHandler

from src.application.common.dto import DTO
from src.application.project.dto import ProjectDTO, UploadProjectDTO
from src.application.project.interfaces import ProjectRepo
from src.infrastructure.db.uow import UnitOfWork


class UploadProject(DTO, Command[ProjectDTO]):
    user_id: int
    project: UploadProjectDTO


class UploadProjectHandler(CommandHandler[UploadProject, ProjectDTO]):
    def __init__(self, repo: ProjectRepo, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    async def __call__(self, command: UploadProject) -> ProjectDTO:
        result = await self.repo.insert_one(user_id=command.user_id, project=command.project)
        await self.uow.commit()

        return result
