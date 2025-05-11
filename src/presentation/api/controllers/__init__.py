from typing import Iterable

from fastapi import FastAPI, APIRouter

from src.presentation.api.controllers.auth import routers as auth_routers
from src.presentation.api.controllers.user import routers as user_routers
from src.presentation.api.controllers.image import routers as image_routers
from src.presentation.api.controllers.project import routers as project_routers
from src.presentation.api.controllers.chat import routers as chat_routers
from src.presentation.api.controllers.google_drive import routers as google_drive_routers


def _include_routers(app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        app.include_router(router)


def setup_routers(app: FastAPI):
    _include_routers(app, auth_routers)
    _include_routers(app, user_routers)
    _include_routers(app, image_routers)
    _include_routers(app, project_routers)
    _include_routers(app, chat_routers)
    _include_routers(app, google_drive_routers)
