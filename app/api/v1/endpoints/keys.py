from fastapi import APIRouter, Path, Depends
from app.models.api_key_model import APIKeyOut
from app.core.dependencies import get_current_user

router = APIRouter()

@router.post("/{project_id}/keys", response_model=APIKeyOut)
async def create_key(project_id: str, current_user=Depends(get_current_user)):
    # Generate API key and insert into DB
    return {
        "id": "key123", "project_id": project_id, "key": "abc123",
        "name": "default", "is_active": True, "created_at": "2025-01-01T00:00:00"
    }