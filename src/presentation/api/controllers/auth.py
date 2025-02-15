from fastapi import APIRouter, Depends, Response, status

from src.application.auth.commands.register_user import RegisterUser
from src.application.auth.queries.login_user import LoginUser

from src.presentation.api.providers.dependency import MediatorDep


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

routers = (auth_router, )


@auth_router.post(
    "/login",
    status_code=status.HTTP_204_NO_CONTENT
)
async def login(
        mediator: MediatorDep,
        data: LoginUser
):
    token = await mediator.query(data)
    response = Response(status_code=status.HTTP_204_NO_CONTENT)

    response.set_cookie(
        "access_token",
        value=token,
        expires=4666666
    )

    return response


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
async def register(
        mediator: MediatorDep,
        data: RegisterUser
):
    await mediator.send(data)


@auth_router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT
)
async def logout():
    response = Response()

    response.set_cookie(
        "access_token",
        value="",
        expires=0
    )

    return response
