"""create_task_tag_table

Revision ID: 6ee6ffc0e32e
Revises: 8ebb9db8ec6e
Create Date: 2023-07-13 16:38:29.963525

"""
from alembic import op

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ee6ffc0e32e'
down_revision = '8ebb9db8ec6e'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('task_tag',
    sa.Column('task_id', sa.BIGINT(), sa.ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('tag_id', sa.BIGINT(), sa.ForeignKey('tag.id', ondelete='CASCADE', onupdate='CASCADE')),
    )

def downgrade() -> None:
    op.drop_table('task_tag')
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