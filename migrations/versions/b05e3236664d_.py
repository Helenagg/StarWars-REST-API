"""empty message

Revision ID: b05e3236664d
Revises: afa6ea1f1a54
Create Date: 2022-12-09 10:28:08.589113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b05e3236664d'
down_revision = 'afa6ea1f1a54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favpeople',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_people', sa.Integer(), nullable=True),
    sa.Column('people_fav', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_fav'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id_people'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favplanet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_plan', sa.Integer(), nullable=True),
    sa.Column('planet_fav', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_fav'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id_plan'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favplanet')
    op.drop_table('favpeople')
    op.drop_table('favorites')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
