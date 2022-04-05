"""create_version_table

Revision ID: dcdda0bc09a7
Revises: e5b0f7bd3466
Create Date: 2022-03-13 02:29:52.851914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcdda0bc09a7'
down_revision = 'e5b0f7bd3466'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'version',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('version', sa.String(120), nullable=False),
        sa.Column('running', sa.String(120), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('version')
