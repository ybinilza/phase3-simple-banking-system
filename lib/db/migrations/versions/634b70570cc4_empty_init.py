"""Empty Init

Revision ID: 634b70570cc4
Revises: bb67ca03682a
Create Date: 2023-09-08 12:33:37.208415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '634b70570cc4'
down_revision: Union[str, None] = 'bb67ca03682a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
