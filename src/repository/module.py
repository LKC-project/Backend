from typing import Type

from src.models.module import ModuleORM

from .base import BaseRepository


class ModuleRepository(BaseRepository[ModuleORM]):
    model: Type[ModuleORM] = ModuleORM
