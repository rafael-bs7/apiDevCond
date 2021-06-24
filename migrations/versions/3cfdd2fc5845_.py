"""empty message

Revision ID: 3cfdd2fc5845
Revises: 
Create Date: 2021-06-18 17:27:44.519356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cfdd2fc5845'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('allowed', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('cover', sa.String(length=50), nullable=False),
    sa.Column('days', sa.String(length=100), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tile', sa.String(length=50), nullable=False),
    sa.Column('file_url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('id_ower', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('cpf', sa.String(length=13), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('wall',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('body', sa.String(length=100), nullable=False),
    sa.Column('datecreated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warning',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('datecreated', sa.Date(), nullable=False),
    sa.Column('photos', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('area_disabled_day',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_areas', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_areas'], ['area.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('billet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('fileurl', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('found_and_lost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_unit', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('where', sa.String(length=50), nullable=False),
    sa.Column('datecreated', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_unit'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_unit', sa.Integer(), nullable=False),
    sa.Column('id_area', sa.Integer(), nullable=False),
    sa.Column('reservation_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_area'], ['area.id'], ),
    sa.ForeignKeyConstraint(['id_unit'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_unit', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_unit'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_unit', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('race', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['id_unit'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_unit', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('color', sa.String(length=20), nullable=False),
    sa.Column('plate', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['id_unit'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wall_like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_wall', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['id_wall'], ['wall.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wall_like')
    op.drop_table('unit_vehicles')
    op.drop_table('unit_pet')
    op.drop_table('unit_people')
    op.drop_table('reservation')
    op.drop_table('found_and_lost')
    op.drop_table('billet')
    op.drop_table('area_disabled_day')
    op.drop_table('warning')
    op.drop_table('wall')
    op.drop_table('user')
    op.drop_table('unit')
    op.drop_table('doc')
    op.drop_table('area')
    # ### end Alembic commands ###
