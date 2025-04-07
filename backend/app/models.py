from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from app.db import Base


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, server_default=func.now(), onupdate=func.now())

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)
    google_id = Column(String, nullable=True)
    google_token = relationship("UserGoogleToken", back_populates="user")
    
class UserGoogleToken(Base, TimestampMixin):
    __tablename__ = "user_google_tokens"
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String)  
    expires_at = Column(DateTime)
    user = relationship("User", back_populates="google_token")

class TempOAuthSession(Base, TimestampMixin):
    __tablename__ = "temp_oauth_sessions"
    
    session_id = Column(String, primary_key=True)
    token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)