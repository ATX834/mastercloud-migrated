from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    async def get_by_google_id(self, google_id: str) -> User | None:
        return self.db.query(User).filter(User.google_id == google_id).first()

    async def create(self, user_in: UserCreate | dict[str, any], google_id: Optional[str] = None) -> User:
        hashed_password = None
        if isinstance(user_in, UserCreate) and user_in.password:
            hashed_password = get_password_hash(user_in.password)
            email=user_in.email
        elif isinstance(user_in, dict):
            email=user_in.get('email')
        else:
            if isinstance(user_in, UserCreate):
                email=user_in.email
            else:
                raise ValueError("Invalid input for user creation")

        existing_user = self.get_by_email(email=email)
        if existing_user:
            if google_id and not existing_user.google_id:
                existing_user.google_id = google_id
                self.db.add(existing_user)
                self.db.commit()
                self.db.refresh(existing_user)
                return existing_user
            return existing_user

        db_user = User(
            email=email,
            hashed_password=hashed_password,
            google_id=google_id,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def list(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.db.query(User).offset(skip).limit(limit).all() 