"""add comments table

Revision ID: 4140272cf905
Revises: 289e9a174d38
Create Date: 2024-06-05 11:03:08.499418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4140272cf905'
down_revision = '289e9a174d38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
