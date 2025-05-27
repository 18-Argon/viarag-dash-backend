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
        price_per_1k = get_current_rate(model=log.model, endpoint=log.endpoint)
        db.execute(
            """
            INSERT
            INTO
            usage_logs(
                api_key_id, project_id, endpoint, token_type, tokens_used,
                success, timestamp, price_per_1k
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                log.api_key_id, log.project_id, log.endpoint, log.token_type,
                log.tokens_used, log.success, timestamp, price_per_1k
            )
        )
        db.commit()
        return {
            "status": "success",
            "project_id": log.project_id,
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
            SELECT id, api_key_id, project_id, endpoint, token_type, tokens_used, success, timestamp, price_per_1k
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
                success=bool(row[6]),
                timestamp=row[7],
                price_per_1k=row[8]
            ) for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
