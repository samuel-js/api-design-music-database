"""empty message

Revision ID: f645eb6a8e68
Revises: 6a7c229ee6f3
Create Date: 2020-02-07 01:44:29.919752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f645eb6a8e68'
down_revision = '6a7c229ee6f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Genre')
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
    op.drop_constraint('Artist_genre_id_fkey', 'Artist', type_='foreignkey')
    op.drop_column('Artist', 'genre_id')
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
    op.drop_constraint('Venue_genre_id_fkey', 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'genre_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Venue_genre_id_fkey', 'Venue', 'Genre', ['genre_id'], ['id'])
    op.drop_column('Venue', 'genres')
    op.add_column('Artist', sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Artist_genre_id_fkey', 'Artist', 'Genre', ['genre_id'], ['id'])
    op.drop_column('Artist', 'genres')
    op.create_table('Genre',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Genre_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Genre_pkey')
    )
    # ### end Alembic commands ###