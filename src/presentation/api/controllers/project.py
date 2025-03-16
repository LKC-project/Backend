from typing import Annotated, Sequence

from fastapi import APIRouter, Path, status

from src.application.project.dto import ProjectDTO, UploadProjectDTO, UpdateProjectDTO
from src.application.project.commands.upload_project import UploadProject
from src.application.project.commands.update_project import UpdateProject
from src.application.project.queries.get_projects_by_user_id import GetProjectsByUserID
from src.application.project.queries.get_project import GetProjectByID

from src.presentation.api.providers.dependency import MediatorDep, CurrentUserIDDep, CurrentUserDep
from src.presentation.api.exceptions import EXCEPTION_RESPONSE_MODEL


project_router = APIRouter(prefix="/project", tags=["Projects"])
projects_router = APIRouter(prefix="/projects", tags=["Projects"])

routers = (project_router, projects_router)


@projects_router.get(
    "/@my",
    description="Повертає список проєктів поточного користувача"
)
async def get_my_projects(
        mediator: MediatorDep,
        current_user_id: CurrentUserIDDep
) -> Sequence[ProjectDTO]:
    return await mediator.query(GetProjectsByUserID(user_id=current_user_id))


@projects_router.get(
    "/{id}",
    description="Повертає об'єкт проєкту",
    dependencies=[CurrentUserDep]
)
async def get_project(
        mediator: MediatorDep,
        id: Annotated[int, Path()]
) -> ProjectDTO | None:
    return await mediator.query(GetProjectByID(id=id))


@project_router.post(
    "",
    description="Створює новий проєкт",
    responses={
        status.HTTP_401_UNAUTHORIZED: EXCEPTION_RESPONSE_MODEL
    },
    status_code=status.HTTP_201_CREATED
)
async def post_project(
        mediator: MediatorDep,
        current_user_id: CurrentUserIDDep,
        project: UploadProjectDTO
) -> ProjectDTO:
    return await mediator.send(UploadProject(user_id=current_user_id, project=project))


@project_router.patch(
    "/{id}",
    description="Оновлення проєкту",
    responses={
        status.HTTP_401_UNAUTHORIZED: EXCEPTION_RESPONSE_MODEL
    },
    status_code=status.HTTP_204_NO_CONTENT
)
async def patch_project(
        mediator: MediatorDep,
        current_user_id: CurrentUserIDDep,
        id: Annotated[int, Path()],
        project: UpdateProjectDTO
) -> None:
    return await mediator.send(UpdateProject(id=id, user_id=current_user_id, project=project))
