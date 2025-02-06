"""Initial

Revision ID: 01c54f4ec2e3
Revises: eed3ee3d505a
Create Date: 2025-01-13 17:09:21.280038

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "01c54f4ec2e3"
down_revision: Union[str, None] = "eed3ee3d505a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "Module", sa.Column("description", sa.String(length=256), nullable=False)
    )


def downgrade() -> None:
    op.drop_column("Module", "description")
