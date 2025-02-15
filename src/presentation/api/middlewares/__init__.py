from fastapi import FastAPI

from src.presentation.api.middlewares.app_error import AppErrorHandlerMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(AppErrorHandlerMiddleware)
