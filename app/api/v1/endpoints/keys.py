from fastapi import APIRouter, Path, Depends, HTTPException, status, Query
from app.models.api_key_model import APIKeyOut
from app.core.dependencies import get_current_user, require_internal_auth
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


@router.get("/validate-key", response_model=dict, dependencies=[Depends(require_internal_auth)])
async def validate_api_key_internal(
    key: str = Query(...)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, project_id, is_active, created_at
        FROM api_keys
        WHERE key = ?
        """,
        (key,)
    )
    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=401, detail="Invalid API key")

    if not row["is_active"]:
        raise HTTPException(status_code=403, detail="API key is inactive")

    return {
        "valid": True,
        "api_key_id": row["id"],
        "project_id": row["project_id"],
        "created_at": row["created_at"],
    }
