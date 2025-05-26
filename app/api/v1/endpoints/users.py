from fastapi import APIRouter, Depends, HTTPException, Path
from app.core.dependencies import get_current_user
from app.services.user_service import get_user, get_or_create_user

router = APIRouter()

@router.get("/me")
def get_my_profile(current_user=Depends(get_current_user)):
    """Returns the authenticated user's profile."""
    return get_user(current_user["user_id"])


@router.post("/init")
def init_user(current_user=Depends(get_current_user)):
    """Creates the user in the users table if not already present."""
    user_id = current_user["user_id"]
    email = current_user["email"]
    get_or_create_user(user_id, email)
    return {"status": "initialized", "user_id": user_id, "email": email}


# @router.get("/{user_id}")
# def get_user_by_id(user_id: str = Path(...)):
#     """Get a user by Firebase UID (admin access or self)."""
#     return get_user(user_id)
#
#
# @router.delete("/{user_id}")
# def delete_user_by_id(user_id: str = Path(...)):
#     """Deletes a user from Firebase. Intended for admin or debug cleanup."""
#     from app.core.firebase import delete_user_by_uid
#     delete_user_by_uid(user_id)
#     return {"status": "deleted", "user_id": user_id}
