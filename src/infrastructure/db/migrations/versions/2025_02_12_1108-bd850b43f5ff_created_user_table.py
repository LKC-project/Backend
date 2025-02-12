"""Created User table

Revision ID: bd850b43f5ff
Revises:
Create Date: 2025-02-12 11:08:05.632791

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bd850b43f5ff"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "User",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=48), nullable=False),
        sa.Column("avatar_url", sa.String(length=256), nullable=False),
        sa.Column("hashed_password", sa.LargeBinary(length=60), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade() -> None:
    op.drop_table("User")
