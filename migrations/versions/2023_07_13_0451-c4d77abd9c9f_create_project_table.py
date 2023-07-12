"""create_project_table

Revision ID: c4d77abd9c9f
Revises: b8b4c329aa9b
Create Date: 2023-07-13 04:51:05.338050

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c4d77abd9c9f'
down_revision = 'b8b4c329aa9b'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
    'project',
    sa.Column('id', sa.BIGINT(), nullable=False, primary_key=True),
    sa.Column('name', sa.VARCHAR(length=100), unique=True),
    sa.Column('site_id', sa.BIGINT(), sa.ForeignKey('site.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('description', sa.TEXT()),
    sa.Column('created_by', sa.BIGINT(), sa.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('updated_by', sa.BIGINT(), sa.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),
    sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.Column('updated_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    )

def downgrade() -> None:
    op.drop_table('project')
    op.drop_table('site_contact')
    op.drop_table('site')
    op.drop_table('user')
    op.drop_table('role')