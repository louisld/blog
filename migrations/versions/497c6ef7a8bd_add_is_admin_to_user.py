"""Add is_admin to user

Revision ID: 497c6ef7a8bd
Revises: 89a2f75b7d5f
Create Date: 2024-12-21 14:34:42.242217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '497c6ef7a8bd'
down_revision = '89a2f75b7d5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'is_admin',
                sa.Boolean(),
                nullable=False,
                server_default='False'
        ))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
