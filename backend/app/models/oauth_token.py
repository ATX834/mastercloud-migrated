from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class OAuthToken(Base):
    __tablename__ = 'oauth_tokens'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    provider = Column(String, nullable=False) # e.g., 'google', 'spotify'
    access_token = Column(String, nullable=False) # Encrypt this!
    refresh_token = Column(String, nullable=True) # Encrypt this!
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="tokens")
