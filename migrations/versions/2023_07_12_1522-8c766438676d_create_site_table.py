"""create_site_table

Revision ID: 8c766438676d
Revises: 7562ce4ac0cf
Create Date: 2023-07-12 15:22:52.874261

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8c766438676d'
down_revision = '7562ce4ac0cf'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('site',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('url', sa.VARCHAR(length=255), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )

def downgrade() -> None:
   op.drop_table('site')