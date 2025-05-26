from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.firebase import verify_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    decoded = verify_token(token)
    if not decoded:
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    return {
        "user_id": decoded["uid"],
        "email": decoded["email"]
    }
