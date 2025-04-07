from datetime import datetime, timedelta, timezone
import uuid
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.models import TempOAuthSession, User, UserGoogleToken
from app.db import get_db
from app.schemas import UserCreate, UserLogin, UserResponse
from app.security import CurrentUser, create_access_token, get_password_hash, verify_password
from app.oauth import oauth
from app.config import settings, fernet

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(email=user.email).first() 
    if existing_user:
        raise HTTPException(status_code=400, detail="Unauthorized")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"} 

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter_by(email=user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="app_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="Strict",
    )

    return response


@router.get("/google/login")
async def google_login(request: Request):    
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback", name="google_callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    google_user = token['userinfo']
    
    existing_user = db.query(User).filter_by(email=google_user.email).first()
    if not existing_user:
        existing_user = User(email=google_user.email, google_id=google_user.sub)
        db.add(existing_user)
        db.commit()

    encrypted_access = fernet.encrypt(token['access_token'].encode())
    encrypted_refresh = fernet.encrypt(token['refresh_token'].encode()) if token.get('refresh_token') else None
    
    db.merge(UserGoogleToken(
        user_id=existing_user.id,
        access_token=encrypted_access,
        refresh_token=encrypted_refresh,
        expires_at=datetime.now(timezone.utc) + timedelta(seconds=token['expires_in'])
    ))
    db.commit()

    access_token = create_access_token(data={"sub": existing_user.email})
    
    session_id = str(uuid.uuid4())

    temp_session = TempOAuthSession(
        session_id=session_id,
        token=access_token,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=3)
    )
    db.add(temp_session)
    db.commit()
    
    return RedirectResponse(url=f"{settings.FRONTEND_URL}/callback?session_id={session_id}")


@router.get("/finalize")
async def auth_finalize(session_id: str, db: Session = Depends(get_db)):
    temp_session = db.query(TempOAuthSession).filter_by(session_id=session_id).first()
    if not temp_session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    access_token = temp_session.token
    db.delete(temp_session)
    db.commit()
    
    response = JSONResponse(content={"message": "Login successful"})
    
    response.set_cookie(
        key="app_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="Strict",
    )
    return response

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(user: CurrentUser):
    return {"user": user}


@router.get("/logout")
async def logout():
    response = JSONResponse({"message": "Logout successful"})
    response.delete_cookie("app_token")
    return response