from fastapi import FastAPI, Path, Query, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from starlette import status

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from models.object_models import Course, Group
from db.db import MyDataBase
from config import DB_NAME, DB_USER, DB_PASS, DB_HOST

db = MyDataBase()
app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
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

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@app.post("/create-course")
async def create_course(course: Course, user: User = Depends(current_user)):
    if user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Данная команда доступна только для преподавателей.",
        )
    await db.add_course(course.owner_id, course.category, course.name, course.is_open, course.sword, course.slug)

@app.post("/create-group")
def create_group(group: Group, user: User = Depends(current_user)):
    if user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Данная команда доступна только для преподавателей.",
        )
    return group

'''
@app.post("/join-course/{course_id}")
async def join_course(course_id, user: User = Depends(current_user)):
    query = course_members.insert().values(id = user.id, role = user.role_id, course_id = course_id)
    await db.execute (query)

    return "Пользователь успешно записан на курс"
'''