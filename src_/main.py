from typing import Iterable

from fastapi import FastAPI, APIRouter, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src_.api.auth import routers as auth_routers
from src_.api.users import routers as users_routers

from src_.config import dev


origins = [
    "*",
    "http://localhost:5174",
    "http://127.0.0.1:5174"
]


app = FastAPI(
    title="LKC-API",
    description="Кря 🦆"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if not dev else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    path="/",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    include_in_schema=False
)
async def root():
    return RedirectResponse(
        url="/docs",
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )


def app_include_routers(_app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        _app.include_router(router)


app_include_routers(app, auth_routers)
app_include_routers(app, users_routers)


if __name__ == "__main__":
    raise NotImplemented
