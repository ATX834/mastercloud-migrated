import logging
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import create_access_token, verify_password
from app.schemas.oauth_token import TokenData
from app.schemas.user import UserCreate, User as UserSchema
from app.api import deps
from app.repositories.user_repository import UserRepository
from app.core.oauth import oauth
from app.core.config import settings

router = APIRouter()
logger = logging.getLogger(__name__)

FRONTEND_LOGIN_URL = "http://localhost:3000/login"  # Définir en variable d'environnement
FRONTEND_CALLBACK_URL = "http://localhost:3000/auth/callback" # Définir en variable d'environnement

@router.post("/token", response_model=TokenData)
async def login_for_access_token(
    repo: UserRepository = Depends(deps.get_user_repository),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = repo.get_by_username(username=form_data.username)
    if not user or not user.hashed_password or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserSchema)
def register_user(
    *,
    repo: UserRepository = Depends(deps.get_user_repository),
    user_in: UserCreate
):
    """Crée un nouvel utilisateur."""
    user = repo.get_by_username(username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = repo.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = repo.create(user_in=user_in)
    return user

@router.get("/google/login")
async def google_login(request: Request):
    redirect_uri = settings.GOOGLE_REDIRECT_URI or request.url_for('google_auth_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/callback", name="google_auth_callback")
async def google_auth_callback(request: Request, repo: UserRepository = Depends(deps.get_user_repository)):
    try:
        token = await oauth.google.authorize_access_token(request)
    except Exception as e:
        logger.error(f"Erreur lors de l'autorisation Google : {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La validation Google a échoué: {e}"
        )

    user_info = token.get('userinfo')
    if not user_info:
        logger.error("Impossible de récupérer les informations de l'utilisateur depuis Google")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Impossible de récupérer les informations de l'utilisateur depuis Google"
        )

    google_id = user_info.get('sub')
    email = user_info.get('email')

    if not email:
        logger.error("L'adresse e-mail n'a pas été fournie par Google")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="L'adresse e-mail n'a pas été fournie par Google"
        )

    try:
        user = await repo.get_by_google_id(google_id=google_id)
        if not user:
            user = await repo.create(user_in=user_info, google_id=google_id)
    except Exception as e:
        logger.error(f"Erreur lors de la création/liaison de l'utilisateur : {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la création/liaison de l'utilisateur: {e}"
        )

    access_token = create_access_token(data={"sub": user.email})
    return RedirectResponse(url=f"{FRONTEND_CALLBACK_URL}#token={access_token}")
