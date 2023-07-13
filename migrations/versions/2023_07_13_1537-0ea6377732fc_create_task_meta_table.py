"""create_task_meta_table

Revision ID: 0ea6377732fc
Revises: 5946eea36baf
Create Date: 2023-07-13 15:37:26.462508

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0ea6377732fc'
down_revision = '5946eea36baf'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('task_meta',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.BIGINT(), sa.ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('meta_key', sa.VARCHAR(length=255), nullable=True),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('task_meta')
    op.drop_table('comment')
    op.drop_table('activity')
    op.drop_table('task')
    op.drop_table('project')
    op.drop_table('site_contact')
    op.drop_table('site')
    op.drop_table('user')
    op.drop_table('role')