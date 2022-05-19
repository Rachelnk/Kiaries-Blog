"""Change name of subcribers' table to subs.

Revision ID: e570f488c85f
Revises: 7ac52eb09ef4
Create Date: 2022-05-18 21:22:53.987526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e570f488c85f'
down_revision = '7ac52eb09ef4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subs_email'), 'subs', ['email'], unique=True)
    op.drop_index('ix_subscribers_email', table_name='subscribers')
    op.drop_table('subscribers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='subscribers_pkey')
    )
    op.create_index('ix_subscribers_email', 'subscribers', ['email'], unique=False)
    op.drop_index(op.f('ix_subs_email'), table_name='subs')
    op.drop_table('subs')
    # ### end Alembic commands ###