from fastapi import APIRouter, Path, Depends, HTTPException, status
from app.models.api_key_model import APIKeyOut
from app.core.dependencies import get_current_user
from app.db.session import get_connection  # ✅ Your DB connection helper
import uuid
import datetime
import sqlite3

router = APIRouter()

@router.post("/{project_id}/keys", response_model=APIKeyOut, status_code=201)
async def create_key(project_id: str, current_user=Depends(get_current_user)):
    conn = get_connection()
    cursor = conn.cursor()

    api_key_id = str(uuid.uuid4())
    api_key = str(uuid.uuid4()).replace("-", "")  # or use secrets.token_hex(16)
    name = "default"
    is_active = True
    created_at = datetime.datetime.utcnow().isoformat()

    try:
        cursor.execute(
            """
            INSERT INTO api_keys (id, project_id, key, name, is_active, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (api_key_id, project_id, api_key, name, is_active, created_at)
        )
        conn.commit()

    except sqlite3.IntegrityError as e:
        # This catches FK constraint errors and unique violations
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create API key: {str(e)}"
        )

    return {
        "id": api_key_id,
        "project_id": project_id,
        "key": api_key,
        "name": name,
        "is_active": is_active,
        "created_at": created_at
    }
