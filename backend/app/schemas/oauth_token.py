# Optional: Schemas for OAuth tokens if you expose related info
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class TokenData(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenInfo(BaseModel):
    provider: str
    expires_at: Optional[datetime] = None
    scopes: List[str] = [] # Scopes granted by the user
