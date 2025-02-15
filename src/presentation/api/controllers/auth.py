from typing import Annotated

from fastapi import APIRouter, Depends, Response
from didiator import Mediator

from src.application.user.commands.create_user import UserCreate
from src.presentation.api.providers.stub import Stub
from src.application.auth.commands.login_user import UserLogin


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

routers = (auth_router, )


@auth_router.post("/login")
async def login(
        mediator: Annotated[Mediator, Depends(Stub(Mediator))],
        data: UserLogin
):
    token = await mediator.send(data)
    response = Response()

    response.set_cookie(
        "access_token",
        value=token,
        expires=4666666
    )

    return response


@auth_router.post("/register")
async def register(
        mediator: Annotated[Mediator, Depends(Stub(Mediator))],
        data: UserCreate
):
    return await mediator.send(data)


@auth_router.post("/logout")
async def logout():
    response = Response()

    response.set_cookie(
        "access_token",
        value="",
        expires=0
    )

    return response
