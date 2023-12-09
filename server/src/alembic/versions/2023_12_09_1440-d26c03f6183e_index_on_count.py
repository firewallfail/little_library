"""index on count

Revision ID: d26c03f6183e
Revises: 8f98f9687706
Create Date: 2023-12-09 14:40:54.199141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd26c03f6183e'
down_revision = '8f98f9687706'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE INDEX idx_count
        ON book (count);
    """)


def downgrade() -> None:
    op.execute("""
        DROP INDEX idx_count ON book;
    """)
