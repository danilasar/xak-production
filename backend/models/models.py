from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, JSON, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("git_password", String, default="", nullable=True)
)

groups = Table('groups',
    metadata,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('owner_id', Integer, nullable=False),
    Column('name', String, nullable=False))

group_members = Table('group_members',
    metadata,
    Column('group_id', Integer, ForeignKey('groups.id'), nullable=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False))

course_categories = Table('course_categories',
    metadata,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('parent_id', Integer, nullable=True),
    Column('name', String, nullable=False),
    Column('desc', String, nullable=False),
    Column('slug', String, nullable=False))

courses = Table('courses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('owner_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('category', Integer, ForeignKey('course_categories.id'), nullable=False),
    Column('name', String, nullable=False),
    Column('is_open', Boolean, nullable=False, default=True),
    Column('sword', String, nullable=True, default=None))

tasks = Table('tasks',
    metadata,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), nullable=True),
    Column('name', String, nullable=False),
    Column('max_grade', Integer, nullable=False, default=100),
    Column('description', String))

course_members = Table('course_members',
    metadata,
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('role', Integer, ForeignKey('role.id'), nullable=False),
    Column('course_id', Integer, ForeignKey('courses.id'), nullable=False))

solutions = Table('task_solutions',
    metadata,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('task_id', Integer, ForeignKey('tasks.id'), nullable=False),
    Column('first_attempt_id', Integer, nullable=True),
    Column('last_attempt_id', Integer, nullable=True),
    Column('attempts_count', Integer, nullable=False),
    Column('is_closed', Boolean, nullable=False, default=False))

attempts = Table('attempts',
    metadata,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('solution_id', Integer, nullable=False),
    Column('number', Integer, nullable=False, default=1),
    Column('mark', Integer, nullable=True),
    Column('mark_desc', String, nullable=True),
    Column('mark_teacher', Integer, nullable=True),
    Column('commit_id', String, nullable=False))

