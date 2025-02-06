from typing import Iterable

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from src.module.router import routers as module_routers
from src.config import dev


origins = [
    "http://localhost:5174",
    "http://127.0.0.1:5174"
]


app = FastAPI(title="API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if not dev else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def app_include_routers(_app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        _app.include_router(router)


app_include_routers(app, module_routers)
