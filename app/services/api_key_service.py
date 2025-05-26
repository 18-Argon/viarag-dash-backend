from app.db.session import get_connection
from fastapi import HTTPException
import sqlite3

def create_api_key(project_id: str, name: str, key: str):
    try:
        with get_connection() as db:
            db.execute(
                """
                INSERT INTO api_keys (project_id, name, key)
                VALUES (?, ?, ?);
                """,
                (project_id, name, key)
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def list_api_keys(project_id: str):
    with get_connection() as db:
        cur = db.execute(
            "SELECT id, name, key FROM api_keys WHERE project_id = ?",
            (project_id,)
        )
        return [{"id": row[0], "name": row[1], "key": row[2]} for row in cur.fetchall()]


def delete_api_key(key_id: str):
    with get_connection() as db:
        db.execute("DELETE FROM api_keys WHERE id = ?", (key_id,))