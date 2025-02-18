from fastapi import APIRouter, Response, status

from src.application.auth.commands.register_user import RegisterUser
from src.application.auth.queries.login_user import LoginUser

from src.presentation.api.providers.dependency import MediatorDep
from src.presentation.api.exceptions import EXCEPTION_RESPONSE_MODEL
from src.presentation.api.providers.auth import auth_provider


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

routers = (auth_router, )


@auth_router.post(
    "/login",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: EXCEPTION_RESPONSE_MODEL
    }
)
async def login(
        mediator: MediatorDep,
        data: LoginUser
):
    user_id = await mediator.query(data)
    response = Response(status_code=status.HTTP_204_NO_CONTENT)

    return auth_provider.login(user_id=user_id, response=response)


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: EXCEPTION_RESPONSE_MODEL
    }
)
async def register(
        mediator: MediatorDep,
        data: RegisterUser
):
    await mediator.send(data)

    return Response(status_code=status.HTTP_201_CREATED)  # Без цього повертається null а не пусте тіло, лол


@auth_router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT
)
async def logout():
    response = Response(status_code=status.HTTP_204_NO_CONTENT)

    return auth_provider.logout(response=response)
