"""Adicionado o campo currency em person

Revision ID: e9776152c02d
Revises: 61a7e25fb5c2
Create Date: 2022-12-29 15:11:33.832811

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'e9776152c02d'
down_revision = '61a7e25fb5c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('currency', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'currency')
    # ### end Alembic commands ###