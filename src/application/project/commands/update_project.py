from didiator import Command, CommandHandler
from orjson import dumps

from src.infrastructure.s3 import ObjectStorage
from src.application.project.dto import DTO, UpdateProjectDTO, UpdateProjectRequestDTO
from src.application.project.interfaces import ProjectRepo
from src.infrastructure.db.uow import UnitOfWork


class UpdateProject(DTO, Command[None]):
    id: int
    user_id: int
    project: UpdateProjectRequestDTO


class UpdateProjectHandler(CommandHandler[UpdateProject, None]):
    def __init__(self, object_storage: ObjectStorage, repo: ProjectRepo, uow: UnitOfWork):
        self.object_storage = object_storage
        self.repo = repo
        self.uow = uow

    async def __call__(self, command: UpdateProject) -> None:
        keys = set(UpdateProjectDTO.__pydantic_fields__.keys())
        update_project = UpdateProjectDTO(**command.project.model_dump(include=keys, exclude_unset=True))

        if bool(update_project.model_dump(exclude_unset=True)):
            await self.repo.update_one(id=command.id, user_id=command.user_id, project=update_project)
            await self.uow.commit()

        name = f"project/{command.id}.json"

        if command.project.content:
            obj = dumps(command.project.content)
            await self.object_storage.put_object(obj, name)
