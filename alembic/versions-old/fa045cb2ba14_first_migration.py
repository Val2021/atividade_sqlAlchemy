"""first migration

Revision ID: fa045cb2ba14
Revises: 77a430c0e603
Create Date: 2021-12-03 11:33:03.087706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa045cb2ba14'
down_revision = '77a430c0e603'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coupons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('expire_at', sa.DateTime(), nullable=True),
    sa.Column('limit', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=15), nullable=True),
    sa.Column('value', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_methods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('price', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('technical_details', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_discounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mode', sa.String(length=45), nullable=True),
    sa.Column('value', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('payment_method_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['payment_method_id'], ['payment_methods.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_discounts')
    op.drop_table('products')
    op.drop_table('suppliers')
    op.drop_table('payment_methods')
    op.drop_table('coupons')
    op.drop_table('categories')
    # ### end Alembic commands ###
