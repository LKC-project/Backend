from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.application.chat.enums import MessageRole
from src.infrastructure.db.models.base import Base


class MessageORM(Base):
    __tablename__ = "Message"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[MessageRole] = mapped_column(Enum(MessageRole))
    content: Mapped[str]


class MessageHistoryORM(Base):
    __tablename__ = "MessageHistory"

    project_id: Mapped[int] = mapped_column(
        ForeignKey("Project.id", ondelete="cascade"),
        primary_key=True
    )
    message_id: Mapped[int] = mapped_column(
        ForeignKey("Message.id", ondelete="cascade"),
        primary_key=True
    )
