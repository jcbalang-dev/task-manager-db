"""create_tag_table

Revision ID: 8ebb9db8ec6e
Revises: aab6ce5c3732
Create Date: 2023-07-13 16:28:50.181517

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8ebb9db8ec6e'
down_revision = 'aab6ce5c3732'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('tag',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=True),
    sa.Column('slug', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('tag')
    op.drop_table('task_label')
    op.drop_table('label')
    op.drop_table('task_meta')
    op.drop_table('comment')
    op.drop_table('activity')
    op.drop_table('task')
    op.drop_table('project')
    op.drop_table('site_contact')
    op.drop_table('site')
    op.drop_table('user')
    op.drop_table('role')