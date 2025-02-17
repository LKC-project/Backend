from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.api.middlewares.app_error import AppErrorHandlerMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(AppErrorHandlerMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
