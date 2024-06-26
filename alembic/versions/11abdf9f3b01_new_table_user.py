"""new_table_user

Revision ID: 11abdf9f3b01
Revises: f2662f23f7eb
Create Date: 2024-06-11 16:31:03.962905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11abdf9f3b01'
down_revision: Union[str, None] = 'f2662f23f7eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('end_date', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('date_format', sa.String(), server_default='weaks', nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.add_column('goals', sa.Column('date_format', sa.String(), server_default='weaks', nullable=True))
    op.add_column('goals', sa.Column('user_id', sa.UUID(), nullable=False))
    op.create_index(op.f('ix_goals_nottodo'), 'goals', ['nottodo'], unique=False)
    op.create_index(op.f('ix_goals_title'), 'goals', ['title'], unique=False)
    op.create_index(op.f('ix_goals_todo'), 'goals', ['todo'], unique=False)
    op.create_index(op.f('ix_goals_user_id'), 'goals', ['user_id'], unique=False)
    op.create_foreign_key(None, 'goals', 'user', ['user_id'], ['id'])
    op.drop_column('goals', 'data_format')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goals', sa.Column('data_format', sa.VARCHAR(), server_default=sa.text("'weaks'::character varying"), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'goals', type_='foreignkey')
    op.drop_index(op.f('ix_goals_user_id'), table_name='goals')
    op.drop_index(op.f('ix_goals_todo'), table_name='goals')
    op.drop_index(op.f('ix_goals_title'), table_name='goals')
    op.drop_index(op.f('ix_goals_nottodo'), table_name='goals')
    op.drop_column('goals', 'user_id')
    op.drop_column('goals', 'date_format')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
