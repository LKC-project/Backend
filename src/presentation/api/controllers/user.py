from typing import Annotated

from fastapi import APIRouter, Path

from src.presentation.api.providers.dependency import MediatorDep


user_router = APIRouter(prefix="/user", tags=["Users"])
users_router = APIRouter(prefix="/users", tags=["Users"])

routers = (user_router, users_router)


@user_router.get("/@me")
async def get_me(

):
    ...


@user_router.get("/{name}")
async def get_user_by_name(
        name: Annotated[str, Path(max_length=48)]
):
    ...


@user_router.get("/{id}")
async def get_user_by_id(
        id: Annotated[int, Path()]
):
    ...
