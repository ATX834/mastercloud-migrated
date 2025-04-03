# app/models/user.py
# Définit le modèle SQLAlchemy pour User.
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# Importe la Base depuis le fichier base.py
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    # Simplification : on suppose que l'identification se fait ailleurs.
    email = Column(String, unique=True, index=True, nullable=False) # Email comme identifiant unique
    hashed_password = Column(String, nullable=True) # Exemple si utilisation d'auth par mot de passe en parallèle
    # Ajoutez d'autres champs de profil utilisateur si nécessaire (ex: nom, image)
    google_id = Column(String, unique=True, nullable=True, index=True) # Si vous stockez l'ID Google
    # is_active = Column(Boolean, default=True) # Si vous avez besoin d'un statut actif/inactif

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relation vers les playlists appartenant à l'utilisateur.
    # Utilise une chaîne "Playlist" pour éviter les imports circulaires.
    playlists = relationship("Playlist", back_populates="owner", cascade="all, delete-orphan")

    # Relation vers les tokens OAuth (si stockés)
    tokens = relationship("OAuthToken", back_populates="user", cascade="all, delete-orphan")

