from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.api.middlewares.app_error import AppErrorHandlerMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(AppErrorHandlerMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173",
                       "http://localhost:5174",
                       "http://127.0.0.1:5173",
                       "http://127.0.0.1:5174",
                       "https://gridium.xyz",
                       "https://lkc-board.xyz"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
