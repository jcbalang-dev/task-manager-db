"""create_label_table

Revision ID: 5974af18bdb1
Revises: 0ea6377732fc
Create Date: 2023-07-13 15:54:35.029016

"""
from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5974af18bdb1'
down_revision = '0ea6377732fc'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('label',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.Column('updated_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
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