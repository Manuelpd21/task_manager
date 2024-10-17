from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import init_db, get_session, engine
from app.schemas import UserCreate, UserRead, TaskCreate, TaskRead
from app.crud import create_user, get_user_by_username, create_task, get_tasks_by_user_id
from app.models import User

# Initialize the database (this should run when the app starts)
init_db()

# Create an instance of FastAPI
app = FastAPI()

# Dependency to get the current database session
def get_db_session():
    with Session(engine) as session:
        yield session

# Define a simple root route
@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Task Manager API"}

# Route to register a new user
@app.post("/users/", response_model=UserRead)
async def register_user(user: UserCreate, db: Session = Depends(get_db_session)) -> UserRead:
    existing_user = get_user_by_username(db, username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db=db, user=user)

from fastapi import Query

@app.post("/tasks/", response_model=TaskRead)
async def create_user_task(
    task: TaskCreate,
    user_id: int = Query(..., description="The ID of the user creating the task"),
    db: Session = Depends(get_db_session)
) -> TaskRead:
    return create_task(db=db, task=task, user_id=user_id)




# Route to get all tasks for a user
@app.get("/tasks/", response_model=list[TaskRead])
async def read_user_tasks(user_id: int, db: Session = Depends(get_db_session)) -> list[TaskRead]:
    tasks = get_tasks_by_user_id(db=db, user_id=user_id)
    return tasks
