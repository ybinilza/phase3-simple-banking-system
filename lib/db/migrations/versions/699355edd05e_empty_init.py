"""Empty Init

Revision ID: 699355edd05e
Revises: f5ebc2fcad88
Create Date: 2023-09-08 23:37:44.516862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '699355edd05e'
down_revision: Union[str, None] = 'f5ebc2fcad88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
