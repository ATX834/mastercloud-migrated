from pydantic_settings import BaseSettings
from typing import Optional
from cryptography.fernet import Fernet

class Settings(BaseSettings):
    PROJECT_NAME: str = "MasterCloud Remaster"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    FRONTEND_URL: Optional[str] = "http://localhost:3000"
    
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_ENCRYPTION_KEY: str
    GOOGLE_REDIRECT_URI: Optional[str] = "http://localhost:8000/api/v1/auth/google/callback"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 

fernet = Fernet(settings.GOOGLE_ENCRYPTION_KEY)
