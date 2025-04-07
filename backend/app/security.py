from datetime import datetime, timedelta, timezone
from typing import Annotated
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.config import settings
from app.models import User 
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)):
    """
    Create a JWT access token
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})               
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_password_hash(password: str) -> str:
    """
    Hash the password with BCrypt
    """ 
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify the password against the hash
    """
    return pwd_context.verify(password, hashed_password)

def get_current_user_from_cookie(token: str, db: Session):
    """
    Récupère l'utilisateur actuel à partir du token dans le cookie.
    """
    credentials_exception = HTTPException(status_code=401, detail="Access refused", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user

def get_current_user(request: Request):
    """
    Récupère l'utilisateur authentifié qui a été attaché dans le middleware.
    """
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
