from fastapi import Request
from app.db import get_db
from app.security import get_current_user_from_cookie
from sqlalchemy.orm import Session

async def auth_middleware(request: Request, call_next):
    token = request.cookies.get("app_token")

    db_generator = get_db()
    db: Session = next(db_generator)

    try:
        if token:
            user = get_current_user_from_cookie(token=token, db=db)
            request.state.user = user
        else:
            request.state.user = None
    except Exception:
        request.state.user = None
    finally:
        db_generator.close()

    response = await call_next(request)
    return response


async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response
