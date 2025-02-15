from typing import Annotated

from fastapi import APIRouter, Path

from src_.services.auth import CurrentUserIDDep


user_router = APIRouter(prefix="/user", tags=["Users"])
users_router = APIRouter(prefix="/users", tags=["Users"])

routers = (user_router, users_router)


@user_router.get("/@me")
async def get_me(
    current_user_id: CurrentUserIDDep
):
    ...


@user_router.get("/{name}")
async def get_user(
        name: Annotated[str, Path(max_length=48)]
):
    ...
