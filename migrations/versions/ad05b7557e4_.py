"""empty message

Revision ID: ad05b7557e4
Revises: 4591499bd6d4
Create Date: 2014-10-07 10:18:58.579908

"""

# revision identifiers, used by Alembic.
revision = 'ad05b7557e4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('processed', sa.Column('duration', sa.Integer(), nullable=True))
    op.add_column('processed', sa.Column('progress', sa.Integer(), nullable=True))
    op.add_column('processed', sa.Column('view_offset', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('processed', 'view_offset')
    op.drop_column('processed', 'progress')
    op.drop_column('processed', 'duration')
    ### end Alembic commands ###
