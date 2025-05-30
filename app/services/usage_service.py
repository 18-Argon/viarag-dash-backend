from datetime import datetime
from typing import List

from fastapi import HTTPException

from app.db.session import get_connection
from app.models.usage_model import UsageLogCreate, UsageLogOut
from app.core.pricing import get_current_rate

def log_usage(log: UsageLogCreate):
    db = get_connection()
    try:
        timestamp = datetime.utcnow().isoformat()

        # Resolve API key metadata
        cursor = db.execute(
            "SELECT id AS api_key_id, project_id FROM api_keys WHERE key = ? AND is_active = 1",
            (log.key,)  # ← make sure this is a single-element tuple
        )
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="API key not found or inactive")

        price_per_1k = get_current_rate(token_type=log.token_type, endpoint=log.endpoint)

        db.execute(
            """
            INSERT INTO usage_logs (
                api_key_id, project_id, endpoint, token_type, tokens_used,
                timestamp, price_per_1k
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["api_key_id"], row["project_id"], log.endpoint, log.token_type,
                log.tokens_used, timestamp, price_per_1k
            )
        )
        db.commit()

        return {
            "success": True,
            "project_id": row["project_id"],
            "token_type": log.token_type,
            "tokens_used": log.tokens_used,
            "logged_at": timestamp
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


def get_usage_logs(project_id: str) -> List[UsageLogOut]:
    db = get_connection()
    try:
        cur = db.execute(
            """
            SELECT id, api_key_id, project_id, endpoint, token_type, tokens_used, timestamp, price_per_1k
            FROM usage_logs WHERE project_id = ? ORDER BY timestamp DESC
            """,
            (project_id,)
        )
        rows = cur.fetchall()
        return [
            UsageLogOut(
                id=row[0],
                api_key_id=row[1],
                project_id=row[2],
                endpoint=row[3],
                token_type=row[4],
                tokens_used=row[5],
                timestamp=row[6],
                price_per_1k=row[7]
            ) for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
