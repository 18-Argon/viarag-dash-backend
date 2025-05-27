from fastapi import Header, HTTPException, status
from app.core.config import INTERNAL_BILLING_SECRET

async def get_user_from_token(authorization: str = Header(...)):
    # Placeholder: In real setup, verify Firebase or session token
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ", 1)[1]
    # Simulated check
    if token != "test-token":
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    return {"user_id": "user_123", "email": "test@example.com"}

async def require_internal_auth(authorization: str = Header(...)):
    expected = f"Bearer {INTERNAL_BILLING_SECRET}"
    if authorization != expected:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized internal request"
        )