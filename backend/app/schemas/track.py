from datetime import datetime
from enum import Enum
from typing import  Optional
from pydantic import BaseModel, ConfigDict, HttpUrl

class TrackSource(str, Enum):
    YOUTUBE = "youtube"
    SPOTIFY = "spotify"


class TrackBase(BaseModel):
    """ Base schema for track data. """
    source_type: TrackSource
    source_id: str
    title: str
    artist: Optional[str] = None
    album: Optional[str] = None
    thumbnail_url: Optional[HttpUrl] = None
    duration_ms: Optional[int] = None

class TrackCreate(BaseModel):
    """ Schema for creating a track, typically via URL. """
    # The backend will parse the URL, determine source_type/source_id,
    # and fetch metadata to populate a full Track record.
    url: HttpUrl # User provides the YouTube or Spotify URL

class Track(TrackBase):
    """ Schema for representing a track in API responses, includes internal ID. """
    id: int
    created_at: datetime

    # Pydantic V2 and later use model_config
    model_config = ConfigDict(from_attributes=True)
    # For Pydantic V1:
    # class Config:
    #     orm_mode = True
