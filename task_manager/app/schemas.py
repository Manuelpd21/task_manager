from pydantic import BaseModel
from typing import Optional

# Schema for creating a new user
class UserCreate(BaseModel):
    username: str
    password: str

# Schema for reading user data (response model)
class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

# Schema for creating a new task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
# Schema for reading task data (response model)
class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True
