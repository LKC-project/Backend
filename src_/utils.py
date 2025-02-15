from typing import Annotated

from fastapi import Depends

from pydantic import BaseModel, Field


class SPagination(BaseModel):
    per_page: int = Field(default=10, ge=1, le=100)
    page: int = Field(default=1, ge=1)

    @property
    def limit(self) -> int:
        return self.per_page

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.per_page


PaginationDep = Annotated[SPagination, Depends()]
