"""Add login lockout columns to User

Revision ID: c4e81f6a2d07
Revises: fe56fa70289e
Create Date: 2026-10-11 11:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4e81f6a2d07'
down_revision = 'fe56fa70289e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'user',
        sa.Column('failed_login_attempts', sa.Integer(), server_default='0', nullable=False),
    )
    op.add_column(
        'user',
        sa.Column('locked_until', sa.DateTime(timezone=True), nullable=True),
    )


def downgrade():
    op.drop_column('user', 'locked_until')
    op.drop_column('user', 'failed_login_attempts')
