"""create_user_table

Revision ID: 7562ce4ac0cf
Revises: ec1c57adbf5e
Create Date: 2023-07-12 13:07:03.004525

"""
from alembic import op

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7562ce4ac0cf'
down_revision = 'ec1c57adbf5e'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column('role_id', sa.BIGINT(), sa.ForeignKey('role.id', ondelete='CASCADE', onupdate='CASCADE')),
        sa.Column('last_name', sa.VARCHAR(length=100)),
        sa.Column('first_name', sa.VARCHAR(length=50)),
        sa.Column('middle_name', sa.VARCHAR(length=100)),
        sa.Column('user_name', sa.VARCHAR(length=100)),
        sa.Column('email', sa.VARCHAR(length=255)),
        sa.Column('password', sa.VARCHAR(length=250)),
        sa.Column('contact_number', sa.VARCHAR(length=20)),
        sa.Column('status', sa.Enum('free', 'basic', 'starter', 'premium')),
        sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    )

def downgrade() -> None:
    op.drop_table('role')
    op.drop_table('user')
