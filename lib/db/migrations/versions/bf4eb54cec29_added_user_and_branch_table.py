"""Added User and Branch table

Revision ID: bf4eb54cec29
Revises: 65d9f10da5fd
Create Date: 2023-09-09 01:19:22.036361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf4eb54cec29'
down_revision: Union[str, None] = '65d9f10da5fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('branch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('branch_address', sa.String(), nullable=True),
    sa.Column('branch_contactno', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('account_type', sa.String(), nullable=True),
    sa.Column('account_balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('branch')
    # ### end Alembic commands ###