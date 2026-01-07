import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Notes API"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "SUPER_SECRET_KEY_123")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()