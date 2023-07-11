"""create_role_table

Revision ID: ec1c57adbf5e
Revises: 
Create Date: 2023-07-11 14:46:32.084636

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ec1c57adbf5e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('role',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('slug', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )


def downgrade() -> None:
    op.drop_table('role')
