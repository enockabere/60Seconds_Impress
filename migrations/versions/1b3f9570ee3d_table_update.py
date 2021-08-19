"""table update

Revision ID: 1b3f9570ee3d
Revises: 9b7ee76b7e7c
Create Date: 2021-08-19 16:40:17.265916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1b3f9570ee3d'
down_revision = '9b7ee76b7e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('working_hours', sa.Integer(), nullable=False),
    sa.Column('breaks', sa.Integer(), nullable=False),
    sa.Column('break_activities', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitchs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitchs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pitchs_pkey')
    )
    op.drop_table('schedules')
    # ### end Alembic commands ###
