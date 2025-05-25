from fastapi import Depends, Header, HTTPException
from app.core.firebase import verify_token

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.split(" ", 1)[1]
    decoded = verify_token(token)
    if not decoded:
        raise HTTPException(status_code=403, detail="Invalid token")
    return {
        "user_id": decoded["uid"],
        "email": decoded.get("email", "")
    }
