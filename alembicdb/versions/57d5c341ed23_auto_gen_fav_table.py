"""auto-gen fav table

Revision ID: 57d5c341ed23
Revises: 4eb5a0571f48
Create Date: 2021-11-26 20:41:17.210523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57d5c341ed23'
down_revision = '4eb5a0571f48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Favorite',
    sa.Column('UserID', sa.Integer(), nullable=False),
    sa.Column('PostID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['PostID'], ['Post.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['UserID'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('UserID', 'PostID')
    )
    op.add_column('Post', sa.Column('content', sa.String(), nullable=False))
    op.drop_column('Post', 'Content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Post', sa.Column('Content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('Post', 'content')
    op.drop_table('Favorite')
    # ### end Alembic commands ###
