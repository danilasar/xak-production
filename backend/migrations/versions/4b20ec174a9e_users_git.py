"""users_git

Revision ID: 4b20ec174a9e
Revises: 5ad0429cdf7b
Create Date: 2024-02-25 11:06:40.004067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b20ec174a9e'
down_revision: Union[str, None] = '5ad0429cdf7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('git_password', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('organisations')
    op.drop_table('group_members')
    op.drop_table('course_categories')
    op.drop_table('users')
    op.drop_table('courses')
    op.drop_table('groups')
    op.drop_table('tasks')
    op.drop_table('attempts')
    op.drop_table('course_members')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_members',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('role', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='course_members_course_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='course_members_user_id_fkey')
    )
    op.create_table('attempts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mark', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mark_desc', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('mark_teacher', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='attempts_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='attempts_pkey')
    )
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('max_grade', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='tasks_course_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
    )
    op.create_table('groups',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('groups_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='groups_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('courses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_open', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('sword', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category'], ['course_categories.id'], name='courses_category_fkey'),
    sa.ForeignKeyConstraint(['owner_id'], ['organisations.id'], name='courses_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='courses_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('git_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='users_role_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('course_categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('desc', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='course_categories_pkey')
    )
    op.create_table('group_members',
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name='group_members_group_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='group_members_user_id_fkey')
    )
    op.create_table('organisations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('admin_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['users.id'], name='organisations_admin_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='organisations_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###