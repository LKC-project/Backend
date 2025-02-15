from typing import Annotated

from fastapi import APIRouter, Query, Depends

from src_.database import SessionDep
from src_.utils import PaginationDep
from src_.repository.module import ModuleRepository

from .schemas import SModulePOST, SModuleFilters


module_router = APIRouter(prefix="/module", tags=["Modules"])
modules_router = APIRouter(prefix="/modules", tags=["Modules"])

routers = (module_router, modules_router)


@module_router.get("/")
async def get_module(
        session: SessionDep,
        id: Annotated[int, Query()]
):
    return await ModuleRepository(session).get_one(id=id)


@modules_router.get("/")
async def get_modules(
        session: SessionDep,
        pagination: PaginationDep,
        filters: Annotated[SModuleFilters, Depends()]
):
    return await ModuleRepository(session).get_many(
        limit=pagination.limit, offset=pagination.offset, **filters.dict(exclude_none=True)
    )


@module_router.post("/")
async def post_module(
        session: SessionDep,
        module_data: SModulePOST
):
    module = await ModuleRepository(session).insert_one(**module_data.dict())
    await session.commit()

    return module


@modules_router.post("/")
async def post_modules(
        session: SessionDep,
        modules_data: list[SModulePOST]
):
    modules = await ModuleRepository(session).insert_many([module.dict() for module in modules_data])
    await session.commit()

    return modules
