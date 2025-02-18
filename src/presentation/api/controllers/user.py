from typing import Annotated

from fastapi import APIRouter, Path, status

from src.application.user.dto import UserDTO
from src.application.user.queries.get_user_by_id import GetUserByID

from src.presentation.api.providers.dependency import MediatorDep, CurrentUserIDDep
from src.presentation.api.exceptions import EXCEPTION_RESPONSE_MODEL


user_router = APIRouter(prefix="/user", tags=["Users"])
users_router = APIRouter(prefix="/users", tags=["Users"])

routers = (user_router, users_router)


@user_router.get(
    "/@me",
    description="Повертає об'єкт авторизованого користувача",
    responses={
        status.HTTP_401_UNAUTHORIZED: EXCEPTION_RESPONSE_MODEL  # noqa: Чого не можна обійтися без цього, щоб додавалося автоматом разом з CurrentUserIDDep 😭😭😭
    }
)
async def get_me(
        mediator: MediatorDep,
        current_user_id: CurrentUserIDDep
) -> UserDTO | None:
    return await mediator.query(GetUserByID(id=current_user_id))


@user_router.get(
    "/{name}",
    name="‼️‼️‼️НЕ РОБИТЬ‼️‼️‼️"
)
async def get_user_by_name(
        name: Annotated[str, Path(max_length=48)]
):
    ...


@user_router.get(
    "/{id}",
    name="‼️‼️‼️НЕ РОБИТЬ‼️‼️‼️"
)
async def get_user_by_id(
        id: Annotated[int, Path()]
):
    ...
