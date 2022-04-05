"""create_qrcode_table

Revision ID: e5b0f7bd3466
Revises: d376f477477f
Create Date: 2022-03-13 02:27:25.838351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b0f7bd3466'
down_revision = 'd376f477477f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'qrcode',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('qrcode', sa.String(255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('qrcode')
