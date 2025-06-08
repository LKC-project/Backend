import time
from typing import Generator

from pytest_asyncio import fixture
from fastapi.testclient import TestClient

from src.main import app


class UserData:
    def __init__(self):
        self.name = str(time.time())
        self.email = f"{time.time()}@example.com"
        self.password = str(time.time())
        self.id = None
        self.project_id = None

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name}, email={self.email}, password={self.password}, "
                f"id={self.id}, project_id={self.project_id})")


@fixture(scope="module")
def user_data() -> UserData:
    user_data = UserData()

    return user_data


@fixture(scope="module")
def client(cookies) -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client


@fixture(scope="module")
def cookies():
    cookies = {}

    return cookies
