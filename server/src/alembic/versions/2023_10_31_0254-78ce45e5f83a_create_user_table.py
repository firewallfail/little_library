"""create user table

Revision ID: 78ce45e5f83a
Revises: 
Create Date: 2023-10-31 02:54:30.423537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78ce45e5f83a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE user (
        id INT NOT NULL AUTO_INCREMENT,
        public_id VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id),
        INDEX (username, public_id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE IF EXISTS user;
    """)
