from pydantic import BaseModel, EmailStr

# Propriétés partagées
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Propriétés pour la création
class UserCreate(UserBase):
    password: str

# Propriétés retournées à l'API
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True 