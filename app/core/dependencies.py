from fastapi import Depends, HTTPException, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.supabase import verify_token
from app.core.config import INTERNAL_BILLING_SECRET

security = HTTPBearer(auto_error=False)

# --- Internal-only Auth ---
def require_internal_auth(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials:
        token = credentials.credentials
        if token == INTERNAL_BILLING_SECRET:
            return {"user_id": "internal", "email": "internal@system.local"}
    raise HTTPException(status_code=403, detail="Unauthorized: internal secret required")

# --- Supabase Authenticated User ---
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials:
        token = credentials.credentials
        decoded = verify_token(token)
        if decoded:
            return {
                "user_id": decoded["uid"],
                "email": decoded.get("email", "")
            }
    raise HTTPException(status_code=403, detail="Unauthorized: invalid or missing token")
