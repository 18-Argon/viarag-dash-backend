from fastapi import HTTPException

from app.db.session import get_connection


def log_usage(api_key: str, tokens_used: int):
    with get_connection() as db:
        cur = db.execute("SELECT id, project_id FROM api_keys WHERE key = ?", (api_key,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=401, detail="Invalid API key")

        db.execute(
            """
            INSERT INTO usage_logs (api_key_id, project_id, tokens_used)
            VALUES (?, ?, ?);
            """,
            (row[0], row[1], tokens_used)
        )


def get_token_usage(project_id: str):
    with get_connection() as db:
        cur = db.execute(
            "SELECT SUM(tokens_used) FROM usage_logs WHERE project_id = ?",
            (project_id,)
        )
        return cur.fetchone()[0] or 0
