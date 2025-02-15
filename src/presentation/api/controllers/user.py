from typing import Annotated

from fastapi import APIRouter, Depends, Path
from didiator import Mediator

from src.presentation.api.providers.stub import Stub
from src.application.user.commands.create_user import UserCreate


user_router = APIRouter(prefix="/user", tags=["Users"])
users_router = APIRouter(prefix="/users", tags=["Users"])

routers = (user_router, users_router)


@user_router.get("/@me")
async def get_me(

):
    ...


@user_router.get("/{name}")
async def get_user(
        name: Annotated[str, Path(max_length=48)]
):
    ...


@user_router.post("")
async def post_user(
        mediator: Annotated[Mediator, Depends(Stub(Mediator))],
        data: UserCreate
):
    return await mediator.send(data)
