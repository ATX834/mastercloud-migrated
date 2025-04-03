# app/models/playlist.py
# Définit le modèle SQLAlchemy pour Playlist.

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# Importe la Base et la table d'association depuis base.py
from app.db.base import Base
from app.models.associations import playlist_track_association

class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False) # Lien vers l'utilisateur propriétaire
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relation vers le propriétaire (User).
    # Utilise une chaîne "User" pour éviter les imports circulaires.
    owner = relationship("User", back_populates="playlists")

    # Relation Many-to-many avec Track, utilisant la table d'association.
    # 'secondary' pointe vers la table d'association importée.
    # 'order_by' assure que les pistes sont chargées dans le bon ordre.
    # Utilise une chaîne "Track" pour éviter les imports circulaires.
    tracks = relationship(
        "Track",
        secondary=playlist_track_association,
        # backref="playlists", # backref peut être défini ici ou dans Track, mais pas les deux. back_populates est préféré.
        order_by=playlist_track_association.c.position, # Ordonne les pistes par leur position
        # lazy='selectin' # Exemple de stratégie de chargement
        back_populates="playlists" # Assurez-vous d'avoir une relation correspondante dans Track si vous avez besoin de naviguer de Track à Playlist
    )

# Si vous définissez back_populates="playlists" ici, vous devez ajouter la relation correspondante dans le modèle Track:
# Dans app/models/track.py, ajoutez dans la classe Track:
# playlists = relationship(
#     "Playlist",
#     secondary=playlist_track_association,
#     back_populates="tracks"
# )
# Cependant, si vous n'avez pas besoin de naviguer de Track vers ses Playlists, cette partie dans Track n'est pas nécessaire.
