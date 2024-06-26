"""added todo notodo

Revision ID: df97648f328d
Revises: 2aaed9f8e6fe
Create Date: 2024-06-07 22:14:16.795332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df97648f328d'
down_revision: Union[str, None] = '2aaed9f8e6fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goals', sa.Column('todo', sa.String(), nullable=False))
    op.add_column('goals', sa.Column('nottodo', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goals', 'nottodo')
    op.drop_column('goals', 'todo')
    # ### end Alembic commands ###
