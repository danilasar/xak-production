from fastapi import FastAPI, Path, Query, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from starlette import status

from auth.auth import auth_backend
from auth.database import Users
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from git.auth import git_login_as_god
from models.object_models import Course, Group
from db.db import MyDataBase

db = MyDataBase()
app = FastAPI()

fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/gitlab-test")
def gitlab_test():
    gl = git_login_as_god()
    users = gl.users.list()
    print(users)
    return f"Hello"
  
@app.post("/create-course", summary="Создание нового курса (Только преподаватель).", tags=["Courses"])
def create_course(course: Course, user: Users = Depends(current_user)):
    if user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Данная команда доступна только для преподавателей.",
        )
    db.add_course(owner_id= user.id, category=course.category, name=course.name, is_open=course.is_open, sword=course.sword)
    return f"Course {course.name} created successfully"


@app.post("/create-group", summary="Создание новой группы (Только преподаватель).", tags=["Groups"])
def create_group(group: Group, user: Users = Depends(current_user)):
    if user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Данная команда доступна только для преподавателей.",
        )
    db.add_group(owner_id=user.id, members_id=group.members, name=group.name)
    return f"Group {group.name} created successfully"


@app.post("/join-course/{course_id}", summary="Присоединение к курсу", tags=["Courses"])
def join_course(course_id, user: Users = Depends(current_user)):
    db.join_course(user.id, user.role_id, course_id)
    return "Пользователь успешно записан на курс"

@app.post("/create-task/{course_id}", summary="Создание заданий на курсе (Только преподаватель)", tags=["Courses"])
def create_task(course_id, name, max_grade, description, user: Users = Depends(current_user)):
    if user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Данная команда доступна только для преподавателей.",
        )
    db.create_task(course_id, name, max_grade, description)
    return "Задание успешно создано"

