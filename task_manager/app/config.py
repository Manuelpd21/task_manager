from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql://root:12345678@localhost:3306/task_manager_db"
    JWT_SECRET_KEY: str = "your_jwt_secret_key"

settings = Settings()
