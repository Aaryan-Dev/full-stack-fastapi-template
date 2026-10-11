"""Add index on item (owner_id, created_at)

Revision ID: b7c3a1d94e52
Revises: fe56fa70289e
Create Date: 2026-10-11 10:00:00.000000

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b7c3a1d94e52'
down_revision = 'fe56fa70289e'
branch_labels = None
depends_on = None

INDEX_NAME = 'ix_item_owner_id_created_at'


def upgrade():
    # CONCURRENTLY avoids holding a write lock on "item" while the index is built,
    # but cannot run inside a transaction block.
    with op.get_context().autocommit_block():
        op.create_index(
            INDEX_NAME,
            'item',
            ['owner_id', 'created_at'],
            unique=False,
            postgresql_concurrently=True,
            if_not_exists=True,
        )


def downgrade():
    with op.get_context().autocommit_block():
        op.drop_index(
            INDEX_NAME,
            table_name='item',
            postgresql_concurrently=True,
            if_exists=True,
        )
