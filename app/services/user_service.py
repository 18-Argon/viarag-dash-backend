from app.db.session import get_connection
from fastapi import HTTPException


def get_or_create_user(user_id: str, email: str):
    db = get_connection()
    try:
        cur = db.execute("SELECT uid FROM users WHERE uid = ?", (user_id,))
        if cur.fetchone():
            return
        db.execute("INSERT INTO users (uid, email) VALUES (?, ?)", (user_id, email))
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


def get_user(user_id: str):
    db = get_connection()
    try:
        cur = db.execute("SELECT uid, email, created_at FROM users WHERE uid = ?", (user_id,))
        row = cur.fetchone()
        if row:
            return {"id": row[0], "email": row[1], "created_at": row[2]}
        raise HTTPException(status_code=404, detail="User not found")
    finally:
        db.close()
