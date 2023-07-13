"""create_comment_table

Revision ID: 5946eea36baf
Revises: fef7cf79e908
Create Date: 2023-07-13 14:47:58.739378

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5946eea36baf'
down_revision = 'fef7cf79e908'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('comment',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('activity_id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.Column('updated_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('comment')
    op.drop_table('activity')
    op.drop_table('task')
    op.drop_table('project')
    op.drop_table('site_contact')
    op.drop_table('site')
    op.drop_table('user')
    op.drop_table('role')