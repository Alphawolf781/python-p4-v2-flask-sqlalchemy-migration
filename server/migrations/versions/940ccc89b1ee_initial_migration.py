"""Initial migration.

Revision ID: 940ccc89b1ee
Revises: 
Create Date: 2024-10-01 14:39:19.504399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '940ccc89b1ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
