from didiator import Command, CommandHandler

from src.infrastructure.s3 import ObjectStorage
from src.application.project.dto import DTO, UpdateProjectDTO
from src.application.project.interfaces import ProjectRepo
from src.infrastructure.db.uow import UnitOfWork


class UpdateProject(DTO, Command[None]):
    id: int
    user_id: int
    project: UpdateProjectDTO


class UpdateProjectHandler(CommandHandler[UpdateProject, None]):
    def __init__(self, object_storage: ObjectStorage, repo: ProjectRepo, uow: UnitOfWork):
        self.object_storage = object_storage
        self.repo = repo
        self.uow = uow

    async def __call__(self, command: UpdateProject) -> None:
        if bool(command.project.model_dump(exclude_unset=True)):
            await self.repo.update_one(id=command.id, user_id=command.user_id, project=command.project)
            await self.uow.commit()
