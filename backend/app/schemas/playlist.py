from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from backend.app.schemas.track import Track


class PlaylistBase(BaseModel):
    """ Base schema for playlist data. """
    name: str = Field(..., min_length=1, max_length=100) # Example validation
    description: Optional[str] = Field(None, max_length=500)

class PlaylistCreate(PlaylistBase):
    """ Schema used when creating a new playlist. """
    pass # Inherits name and description from PlaylistBase

class PlaylistUpdate(PlaylistBase):
    """ Schema used when updating an existing playlist. All fields optional. """
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class PlaylistTrackAssociation(BaseModel):
    """ Schema representing a track within a playlist, including its position. """
    position: int
    added_at: datetime
    track: Track # Embed the full track details

    # Pydantic V2 and later use model_config
    model_config = ConfigDict(from_attributes=True)
    # For Pydantic V1:
    # class Config:
    #     orm_mode = True

class Playlist(PlaylistBase):
    """ Schema for representing a full playlist in API responses. """
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    # The tracks list will be populated based on the relationship and ordered by position
    # Note: This structure assumes you resolve the association details in your endpoint logic
    tracks: List[Track] = [] # List of tracks included in the playlist response

    # Pydantic V2 and later use model_config
    model_config = ConfigDict(from_attributes=True)
    # For Pydantic V1:
    # class Config:
    #     orm_mode = True

class PlaylistWithTrackDetails(Playlist):
    """
    Alternative Playlist schema that includes association details (position, added_at)
    for each track, if needed by the frontend.
    """
    # This requires more complex query logic to construct
    tracks_with_details: List[PlaylistTrackAssociation] = []

    # Pydantic V2 and later use model_config
    model_config = ConfigDict(from_attributes=True)
    # For Pydantic V1:
    # class Config:
    #     orm_mode = True

