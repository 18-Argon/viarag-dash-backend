from fastapi import Depends, HTTPException, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.firebase import verify_token
import os

security = HTTPBearer(auto_error=False)  # Don't auto-raise on missing token

INTERNAL_SECRET = os.getenv("INTERNAL_BILLING_SECRET")

def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    authorization: str = Header(default=None)
):
    # 🔐 Case 1: Internal secret-based auth
    if authorization == f"Bearer {INTERNAL_SECRET}":
        return {
            "user_id": "internal",
            "email": "internal@system.local"
        }

    # 🔐 Case 2: Firebase Bearer token
    if credentials:
        token = credentials.credentials
        decoded = verify_token(token)
        if decoded:
            return {
                "user_id": decoded["uid"],
                "email": decoded["email"]
            }

    # ❌ If neither works
    raise HTTPException(status_code=403, detail="Invalid or missing authentication")
