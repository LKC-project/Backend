from typing import Annotated

from fastapi import FastAPI, Path

from src.test.dto import CounterDTO


app = FastAPI()


@app.get("/counter/{id}")
async def get_counter(
        id: Annotated[int, Path()]
) -> CounterDTO:
    return {}


@app.post("/counter")
async def post_counter() -> CounterDTO:
    return {}


@app.patch("/counter/{id}")
async def patch_counter(
        id: Annotated[int, Path()]
) -> CounterDTO:
    return {}
