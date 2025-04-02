from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.session import SessionLocal
from app.repositories.user_repository import UserRepository

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db) 