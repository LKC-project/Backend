"""Initial

Revision ID: eed3ee3d505a
Revises: 
Create Date: 2025-01-12 23:56:52.358748

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "eed3ee3d505a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Module",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=48), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("Module")
