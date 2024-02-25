from pydantic import BaseModel

class Course(BaseModel):
    owner_id: int
    category: int
    name: str
    is_open: int
    sword: str

class Group(BaseModel):
    owner_id: int
    members: list
    name: str

