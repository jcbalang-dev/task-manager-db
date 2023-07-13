"""create_task_label_table

Revision ID: aab6ce5c3732
Revises: 5974af18bdb1
Create Date: 2023-07-13 16:22:25.340690

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'aab6ce5c3732'
down_revision = '5974af18bdb1'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('task_label',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.BIGINT(), sa.ForeignKey('task.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('label_id', sa.BIGINT(), sa.ForeignKey('label.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True, unique=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.Column('updated_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
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