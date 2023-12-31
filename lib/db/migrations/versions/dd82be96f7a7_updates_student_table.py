"""updates student table

Revision ID: dd82be96f7a7
Revises: 653d51c81139
Create Date: 2023-09-09 23:11:47.421697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd82be96f7a7'
down_revision: Union[str, None] = '653d51c81139'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('branch', sa.Column('branch_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('branch', 'branch_name')
    # ### end Alembic commands ###
