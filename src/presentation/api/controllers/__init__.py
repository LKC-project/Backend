from typing import Iterable

from fastapi import FastAPI, APIRouter

from src.presentation.api.controllers.user import routers as user_routers
from src.presentation.api.controllers.auth import routers as auth_routers


def _include_routers(app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        app.include_router(router)


def setup_routers(app: FastAPI):
    _include_routers(app, user_routers)
    _include_routers(app, auth_routers)
