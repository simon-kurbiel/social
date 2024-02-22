"""create posts table

Revision ID: 9adc8f5c52bf
Revises: 
Create Date: 2024-02-21 23:47:09.809592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9adc8f5c52bf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
                    sa.Column('title', sa.String(100), nullable=False)
                    )
    
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
