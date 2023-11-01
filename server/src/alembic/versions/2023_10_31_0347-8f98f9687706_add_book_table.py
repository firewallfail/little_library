"""add book table

Revision ID: 8f98f9687706
Revises: 78ce45e5f83a
Create Date: 2023-10-31 03:47:27.368400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f98f9687706'
down_revision = '78ce45e5f83a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE book (
        id INT NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        upc VARCHAR(255) NOT NULL,
        count TINYINT UNSIGNED NOT NULL,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id),
        INDEX (upc)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE IF EXISTS book;
    """)
