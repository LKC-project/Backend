from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class ModuleORM(Base):
    __tablename__ = "Module"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=48))
    description: Mapped[str] = mapped_column(String(length=256))
