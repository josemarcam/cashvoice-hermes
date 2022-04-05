"""add_qrcode_column_to_user_table

Revision ID: 51db65a34861
Revises: dcdda0bc09a7
Create Date: 2022-03-13 02:33:23.415581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51db65a34861'
down_revision = 'dcdda0bc09a7'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('qrcode',sa.Column('user_id',  sa.BigInteger))
    op.create_foreign_key(u'user_id', 'qrcode', 'user', ['user_id'], ['id'])

def downgrade():
    op.drop_constraint(u'user_id', 'qrcode', type_='foreignkey')
    op.drop_column('qrcode', 'user_id')