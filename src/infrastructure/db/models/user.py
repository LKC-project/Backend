from sqlalchemy import String, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base


class UserORM(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=48), unique=True)
    avatar_url: Mapped[str] = mapped_column(String(length=256), nullable=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary(length=60))
