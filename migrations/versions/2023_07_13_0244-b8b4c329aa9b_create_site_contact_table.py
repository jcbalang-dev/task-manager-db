"""create_site_contact_table

Revision ID: b8b4c329aa9b
Revises: 8c766438676d
Create Date: 2023-07-13 02:44:43.397718

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b8b4c329aa9b'
down_revision = '8c766438676d'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'site_contact',
        sa.Column('id', sa.BIGINT(), nullable=False, primary_key=True),
        sa.Column('site_id', sa.BIGINT(), sa.ForeignKey('site.id', ondelete='CASCADE', onupdate='CASCADE')),
        sa.Column('last_name', sa.VARCHAR(length=100)),
        sa.Column('first_name', sa.VARCHAR(length=50)),
        sa.Column('middle_name', sa.VARCHAR(length=50)),
        sa.Column('email', sa.VARCHAR(length=255)),
        sa.Column('contact_number', sa.VARCHAR(length=20)),
        sa.Column('subject', sa.VARCHAR(length=100)),
        sa.Column('message', sa.Text()),
        sa.Column('created_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DATETIME(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
    )
    
def downgrade() -> None:
   op.drop_table('site_contact')
   op.drop_table('site')
   op.drop_table('user')
   op.drop_table('role')