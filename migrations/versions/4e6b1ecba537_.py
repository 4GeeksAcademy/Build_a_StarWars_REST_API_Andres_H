"""empty message

Revision ID: 4e6b1ecba537
Revises: a5cffa318ac2
Create Date: 2024-07-03 22:41:29.871144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e6b1ecba537'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('eye_color', sa.String(length=250), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('passengers', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('login_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('subscription_date', sa.Date(), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('user_email_key', ['email'])
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('subscription_date')
        batch_op.drop_column('lastname')
        batch_op.drop_column('name')
        batch_op.drop_column('username')

    op.drop_table('login')
    op.drop_table('favorite__vehicles')
    op.drop_table('favorite__planets')
    op.drop_table('favorite__characters')
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
