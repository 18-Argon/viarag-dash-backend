from app.core.config import FIREBASE_CREDENTIAL_PATH
from fastapi import HTTPException
import firebase_admin
from firebase_admin import auth, credentials
from firebase_admin.auth import InvalidIdTokenError, ExpiredIdTokenError, RevokedIdTokenError, UserNotFoundError


if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIAL_PATH)
    firebase_admin.initialize_app(cred)

def verify_token(token: str) -> dict:
    """
    Verifies a Firebase ID token and returns the decoded claims if valid.

    Args:
        token (str): The Firebase ID token to verify.

    Returns:
        dict: The decoded token claims if valid.

    Raises:
        HTTPException: If the token is invalid, expired, or revoked.
    """
    try:
        return auth.verify_id_token(token)
    except ExpiredIdTokenError:
        raise HTTPException(status_code=401, detail="Expired Firebase ID token.")
    except RevokedIdTokenError:
        raise HTTPException(status_code=401, detail="Revoked Firebase ID token.")
    except InvalidIdTokenError:
        raise HTTPException(status_code=401, detail="Invalid Firebase ID token.")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Unexpected Firebase token error: {str(e)}")


def delete_user_by_uid(uid: str) -> None:
    """
    Deletes a Firebase user by UID.

    Args:
        uid (str): The UID of the Firebase user to delete.

    Raises:
        HTTPException: If the user is not found or deletion fails.
    """
    try:
        auth.delete_user(uid)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail=f"Firebase user with UID '{uid}' not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting Firebase user with UID '{uid}': {str(e)}")
