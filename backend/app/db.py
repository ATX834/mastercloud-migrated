from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.config import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()