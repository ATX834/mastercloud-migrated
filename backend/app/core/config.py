from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Auth"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
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

    # --- Google OAuth Settings ---
    # Ces valeurs DOIVENT être définies dans le fichier .env
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    # L'URI de redirection doit correspondre à celle configurée dans Google Cloud Console
    # et au chemin de notre endpoint de callback.
    # Mettre Optional au cas où on ne veut pas configurer Google OAuth tout de suite
    GOOGLE_REDIRECT_URI: Optional[str] = "http://localhost:8000/api/v1/auth/google/callback"

    class Config:
        case_sensitive = True
        env_file = ".env"
        # Permettre les champs extras si on veut tester sans définir les clés Google
        # extra = 'ignore' # Alternativement, on peut rendre les champs GOOGLE_* Optionnels

settings = Settings() 