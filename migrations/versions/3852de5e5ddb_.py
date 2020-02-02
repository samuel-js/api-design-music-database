"""empty message

Revision ID: 3852de5e5ddb
Revises: ff99535611f1
Create Date: 2020-02-02 14:38:59.901949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3852de5e5ddb'
down_revision = 'ff99535611f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_image_link', sa.String(length=500), nullable=True))
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_image_link'], ['image_link'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'artist_image_link')
    # ### end Alembic commands ###
