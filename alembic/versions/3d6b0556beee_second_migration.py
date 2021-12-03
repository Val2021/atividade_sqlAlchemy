"""Second migration

Revision ID: 3d6b0556beee
Revises: fa045cb2ba14
Create Date: 2021-12-03 19:43:59.141077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d6b0556beee'
down_revision = 'fa045cb2ba14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=True),
    sa.Column('last_name', sa.String(length=45), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('genre', sa.String(length=45), nullable=True),
    sa.Column('document_id', sa.String(length=45), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    op.drop_table('addresses')
    # ### end Alembic commands ###
