# app/models/track.py
# Définit le modèle SQLAlchemy pour Track et l'énumération TrackSource.

import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# Importe la Base depuis le fichier base.py
from app.db.base import Base
from app.models.associations import playlist_track_association

# Enum pour la source de la piste musicale
class TrackSource(enum.Enum):
    YOUTUBE = "youtube"
    SPOTIFY = "spotify"

class Track(Base):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True, index=True)
    # Utilise SQLEnum pour mapper l'Enum Python à la colonne de la base de données
    source_type = Column(SQLEnum(TrackSource), nullable=False, index=True) # ex: YOUTUBE, SPOTIFY
    source_id = Column(String, nullable=False, index=True) # L'ID unique de la source (ex: ID vidéo YouTube, ID piste Spotify)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=True) # L'artiste peut ne pas toujours être disponible ou clairement défini
    album = Column(String, nullable=True) # Info album si disponible
    thumbnail_url = Column(String, nullable=True) # URL de l'image miniature de la piste
    duration_ms = Column(Integer, nullable=True) # Durée en millisecondes
    # Assurer l'unicité basée sur la source et source_id
    __table_args__ = (UniqueConstraint('source_type', 'source_id', name='_source_uc'),)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    playlists = relationship(
        "Playlist",
        secondary=playlist_track_association,
        back_populates="tracks"
    )
    # La relation Many-to-Many avec Playlist est définie dans le modèle Playlist
    # en utilisant la table d'association 'playlist_track_association'.
