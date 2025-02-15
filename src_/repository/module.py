from typing import Type

from src_.models.module import ModuleORM

from .base import BaseRepository


class ModuleRepository(BaseRepository[ModuleORM]):
    model: Type[ModuleORM] = ModuleORM
