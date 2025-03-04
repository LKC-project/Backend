from typing import Sequence

from sqlalchemy import insert, update, select, exists

from src.infrastructure.db.repositories.base import BaseRepo
from src.infrastructure.db.models.project import ProjectORM, UserProjectORM
from src.infrastructure.db.mappers import ProjectMapper
from src.application.common.exceptions.project import ProjectAccessDenied
from src.application.project.interfaces.reader import ProjectReader
from src.application.project.interfaces.repo import ProjectRepo
from src.application.project.dto import ProjectDTO, UploadProjectDTO, UpdateProjectDTO


class ProjectReaderImpl(BaseRepo[ProjectORM], ProjectReader):
    model = ProjectORM
    mapper = ProjectMapper
    association = UserProjectORM

    async def select_all_by_user_id(self, id: int) -> Sequence[ProjectDTO]:
        cte = (
            select(self.association.project_id)
            .where(self.association.user_id == id)
            .cte("project_ids")
        )

        query = (
            select(self.model)
            .where(self.model.id.in_(select(cte)))
        )

        result = await self.session.scalars(query)

        return [self.mapper.from_orm(project) for project in result]

    async def select_all_by_id_and_user_id(self, id: int, user_id: int) -> ProjectDTO | None:
        query = (
            select(self.model)
            .where(
                self.model.id == id,
                exists().where(
                    (self.association.project_id == id) & (self.association.user_id == user_id)
                )
            )
        )

        result = await self.session.scalar(query)

        return None if result is None else self.mapper.from_orm(result)

    async def select_by_id(self, id: int) -> ProjectDTO | None:
        query = (
            select(self.model)
            .where(self.model.id == id)
        )

        result = await self.session.scalar(query)

        return None if result is None else self.mapper.from_orm(result)


class ProjectRepoImpl(BaseRepo[ProjectORM], ProjectRepo):
    model = ProjectORM
    mapper = ProjectMapper
    association = UserProjectORM

    async def insert_one(self, user_id: int, project: UploadProjectDTO) -> ProjectDTO:
        stmt = (
            insert(self.model)
            .values(**self.mapper.to_dict(project))
            .returning(self.model)
        )

        created_project = await self.session.scalar(stmt)

        stmt = (
            insert(self.association)
            .values(project_id=created_project.id, user_id=user_id)
        )

        await self.session.execute(stmt)

        return self.mapper.from_orm(created_project)

    async def update_one(self, id: int, user_id: int, project: UpdateProjectDTO):
        stmt = (
            update(self.model)
            .where(
                self.model.id == id,
                exists().where(
                    (self.association.project_id == id) & (self.association.user_id == user_id)
                )
            )
            .values(**self.mapper.to_dict_exclude_unset(project))
            .returning(self.model)
        )

        result = await self.session.scalar(stmt)

        if result is None:
            raise ProjectAccessDenied
