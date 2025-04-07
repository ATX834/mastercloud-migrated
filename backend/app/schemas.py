from pydantic import BaseModel
from datetime import datetime
class UserBase(BaseModel):
    """ User base schema. """
    email: str

class UserCreate(UserBase):
    """ User create schema. """
    password: str
    
class UserLogin(UserBase):
    """ User login schema. """
    password: str

class UserProfile(UserBase):
    """ User profile schema. """
    id: int
    created_at: datetime
    google_id: str | None = None
  
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    """ User response schema. """
    user: UserProfile

class Token(BaseModel):
    """ Token schema. """
    access_token: str
    
