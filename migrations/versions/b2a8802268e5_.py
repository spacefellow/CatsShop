"""empty message

Revision ID: b2a8802268e5
Revises: 6245a47424ea
Create Date: 2022-09-01 22:42:47.609530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2a8802268e5'
down_revision = '6245a47424ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cat', sa.Column('age', sa.Integer(), nullable=True))
    op.drop_column('cat', 'ages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cat', sa.Column('ages', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('cat', 'age')
    # ### end Alembic commands ###