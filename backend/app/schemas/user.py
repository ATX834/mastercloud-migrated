from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """ Base schema for user data. """
    email: str

class UserCreate(UserBase):
    """ Schema used when creating a new user (e.g., after first OAuth login). """
    # Depending on your auth flow, you might include provider details here
    # or handle it purely based on the OAuth token verification.
    password: Optional[str] = None # Example if allowing password creation too

class User(UserBase):
    """ Schema for representing a user in API responses. """
    id: int
    created_at: datetime
    # Avoid returning sensitive info like hashed_password

    # Pydantic V2 and later use model_config
    model_config = ConfigDict(from_attributes=True)
    # For Pydantic V1:
    # class Config:
    #     orm_mode = True