from abc import ABCMeta

from pydantic import BaseModel


class DTO(BaseModel, metaclass=ABCMeta):
    pass
