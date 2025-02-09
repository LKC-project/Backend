from typing import Annotated

from fastapi import APIRouter, Depends, Request, status

from src.services.auth import auth_service


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

routers = (auth_router, )


@auth_router.post(
    path="/login",
    description="Авторизація користувача",
)
async def login():
    return auth_service.login(1)  # TODO: Mediator


@auth_router.post(
    path="/register",
    description="Реєстрація нового користувача",
    status_code=status.HTTP_201_CREATED
)
async def register():
    ...


@auth_router.post(
    path="/logout",
    description="Logout, lol",
    status_code=status.HTTP_204_NO_CONTENT
)
async def logout():
    return auth_service.logout()  # TODO: Mediator
