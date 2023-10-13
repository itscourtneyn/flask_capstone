"""empty message

Revision ID: 3b43215dd705
Revises: 7f120e3461d9
Create Date: 2023-10-12 16:22:01.146840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b43215dd705'
down_revision = '7f120e3461d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('contributor', sa.String(length=150), nullable=True),
    sa.Column('prep_time', sa.String(length=100), nullable=True),
    sa.Column('rise_time', sa.String(length=100), nullable=True),
    sa.Column('bake_time', sa.String(length=100), nullable=True),
    sa.Column('ingredients', sa.String(length=2000), nullable=True),
    sa.Column('instructions', sa.String(length=2000), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('car')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('vin', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('year', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('make', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('color', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], name='car_user_token_fkey'),
    sa.PrimaryKeyConstraint('vin', name='car_pkey')
    )
    op.drop_table('recipe')
    # ### end Alembic commands ###