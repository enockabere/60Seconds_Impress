"""empty message

Revision ID: d54c2db9cbc2
Revises: 1b3f9570ee3d
Create Date: 2021-08-19 17:11:23.037973

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd54c2db9cbc2'
down_revision = '1b3f9570ee3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitchs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('category', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category'),
    sa.UniqueConstraint('message')
    )
    op.drop_table('schedules')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('working_hours', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('breaks', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('break_activities', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='schedules_pkey')
    )
    op.drop_table('pitchs')
    # ### end Alembic commands ###
