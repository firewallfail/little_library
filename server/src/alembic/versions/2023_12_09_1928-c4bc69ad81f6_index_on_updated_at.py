"""index on updated_at

Revision ID: c4bc69ad81f6
Revises: d26c03f6183e
Create Date: 2023-12-09 19:28:18.030131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4bc69ad81f6'
down_revision = 'd26c03f6183e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE INDEX idx_created_at
        ON book (created_at);
    """)


def downgrade() -> None:
    op.execute("""
        DROP INDEX idx_created_at ON book;
    """)
