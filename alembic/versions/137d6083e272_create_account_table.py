"""create account table

Revision ID: 137d6083e272
Revises: 
Create Date: 2022-08-19 06:18:40.307707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137d6083e272'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('account')
