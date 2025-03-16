from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSON

from src.infrastructure.db.models.base import Base


class ProjectORM(Base):
    __tablename__ = "Project"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255))
    description: Mapped[str | None] = mapped_column(String(length=512))
    content: Mapped[dict] = mapped_column(JSON, nullable=True)


class UserProjectORM(Base):
    __tablename__ = "UserProject"

    project_id: Mapped[int] = mapped_column(
        ForeignKey("Project.id", ondelete="cascade"),
        primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("User.id", ondelete="cascade"),
        primary_key=True
    )

    project: Mapped["ProjectORM"] = relationship()
