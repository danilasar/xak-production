from pydantic import BaseModel

class Course(BaseModel):
    owner_id: int
    category: int
    name: str
    is_open: bool
    sword: str
    slug: str

class Group(BaseModel):
    members: list

