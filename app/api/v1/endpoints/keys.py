from fastapi import APIRouter, Path
from app.models.api_key_model import APIKeyOut

router = APIRouter()

@router.post("/{project_id}/keys", response_model=APIKeyOut)
def create_key(project_id: str):
    # Generate API key and insert into DB
    return {
        "id": "key123", "project_id": project_id, "key": "abc123",
        "name": "default", "is_active": True, "created_at": "2025-01-01T00:00:00"
    }