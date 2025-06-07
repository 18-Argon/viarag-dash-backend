from fastapi import HTTPException
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase configuration. Please set SUPABASE_URL and SUPABASE_KEY in .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def verify_token(token: str) -> dict:
    """
    Verifies a Supabase JWT token and returns the decoded claims if valid.

    Args:
        token (str): The Supabase JWT token to verify.

    Returns:
        dict: The decoded token claims if valid.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        # Supabase client handles token verification internally
        user = supabase.auth.get_user(token)
        return {
            "uid": user.user.id,
            "email": user.user.email
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid or expired token: {str(e)}") 