from sqlalchemy import String, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base


class UserORM(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=48))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    avatar_url: Mapped[str | None] = mapped_column(String(length=256), nullable=True)
    hashed_password: Mapped[bytes | None] = mapped_column(LargeBinary(length=60), nullable=True)
    active: Mapped[bool] = mapped_column(default=True)
