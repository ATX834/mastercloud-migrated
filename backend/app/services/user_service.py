from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import get_password_hash, verify_password

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.repository.get_by_email(email)

    def get_user_by_google_id(self, google_id: str) -> Optional[User]:
        return self.repository.get_by_google_id(google_id)

    def create_user(self, email: str, password: Optional[str] = None, 
                   full_name: Optional[str] = None, google_id: Optional[str] = None) -> User:
        db_user = User(
            email=email,
            hashed_password=get_password_hash(password) if password else None,
            full_name=full_name,
            google_id=google_id
        )
        return self.repository.create(db_user)

    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        user = self.get_user(user_id)
        if not user:
            return None
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        return self.repository.update(user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not user.hashed_password:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user 