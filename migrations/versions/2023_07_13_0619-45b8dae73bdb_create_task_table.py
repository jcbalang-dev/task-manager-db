"""create_task_table

Revision ID: 45b8dae73bdb
Revises: c4d77abd9c9f
Create Date: 2023-07-13 06:19:01.423680

"""
from alembic import op

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45b8dae73bdb'
down_revision = 'c4d77abd9c9f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    'task',
    sa.Column('id',sa.BIGINT(), nullable=False, primary_key=True),
    sa.Column('user_id',sa.BIGINT(), sa.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('title',sa.VARCHAR(50)),
    sa.Column('description',sa.TEXT()),
    sa.Column('attachment',sa.BLOB()),
    sa.Column('status',sa.Enum('pending', 'in progress', 'completed')),
    sa.Column('hours',sa.TIME()),
    sa.Column('project_id',sa.BIGINT(), sa.ForeignKey('project.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('assigned_to',sa.VARCHAR(100)),
    sa.Column('planned_start_date',(sa.DATE())),
    sa.Column('planned_end_date',sa.DATE()),
    sa.Column('actual_start_date',sa.DATE()),
    sa.Column('actual_end_date',sa.DATE()),
    sa.Column('due_date',sa.DATE()),
    sa.Column('priority',sa.INTEGER()),
    sa.Column('created_by',sa.BIGINT(), sa.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('updated_by',sa.BIGINT(), sa.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('created_at',sa.DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    sa.Column('updated_at',sa.DATETIME, server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('task')
    op.drop_table('project')
    op.drop_table('site_contact')
    op.drop_table('site')
    op.drop_table('user')
    op.drop_table('role')