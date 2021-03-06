"""Type add

Revision ID: 995abb77808e
Revises: 21b3d671a45f
Create Date: 2020-03-07 23:54:42.017994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '995abb77808e'
down_revision = '21b3d671a45f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('content', sa.Column('type', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('content', 'type')
    # ### end Alembic commands ###
