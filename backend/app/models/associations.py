from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Table
from app.db.base import Base

playlist_track_association = Table(
    'playlist_track',
    Base.metadata,
    Column('playlist_id', Integer, ForeignKey('playlists.id'), primary_key=True),
    Column('track_id', Integer, ForeignKey('tracks.id'), primary_key=True),
    Column('position', Integer, nullable=False),
    Column('added_at', DateTime(timezone=True), server_default=func.now())
)