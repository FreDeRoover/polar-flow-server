"""Add WHOOP metrics fields to users and exercise tables.

Revision ID: a1b2c3d4e5f6
Revises: f7g8h9i0j1k2
Create Date: 2026-01-14 10:00:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a1b2c3d4e5f6"
down_revision: str | None = "f7g8h9i0j1k2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Add birth_date, max_hr, and vo2_max to users, and muscle_load to exercise."""
    # Add columns to users table
    op.add_column("users", sa.Column("birth_date", sa.Date(), nullable=True))
    op.add_column("users", sa.Column("max_hr", sa.Integer(), nullable=True))
    op.add_column("users", sa.Column("vo2_max", sa.Integer(), nullable=True))

    # Add muscle_load to exercise table
    op.add_column(
        "exercise",
        sa.Column(
            "muscle_load",
            sa.Float(),
            nullable=True,
            comment="Estimated musculoskeletal stress",
        ),
    )


def downgrade() -> None:
    """Remove WHOOP metrics fields."""
    op.drop_column("exercise", "muscle_load")
    op.drop_column("users", "vo2_max")
    op.drop_column("users", "max_hr")
    op.drop_column("users", "birth_date")
