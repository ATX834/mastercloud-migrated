from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.core.config import settings
from app.api.v1.api import api_router
from app.db.session import engine
from app.models.associations import playlist_track_association
from app.models.oauth_token import OAuthToken
from app.models.playlist import Playlist
from app.models.track import Track
from app.models.user import User
from app.db.base import Base 

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configuration CORS
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    # Options de cookie (sécurité) - à ajuster si besoin
    # https_only=True, # Mettre à True si votre app est servie en HTTPS
    # same_site="lax",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À modifier en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes API
app.include_router(api_router, prefix=settings.API_V1_STR) 