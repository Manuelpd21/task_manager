from sqlmodel import SQLModel, Session
from app.models import User, Task  # Ensure models are imported here
from app.config import settings
from sqlmodel import create_engine

engine = create_engine(settings.DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session
