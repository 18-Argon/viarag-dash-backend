import sqlite3
from app.core.config import DATABASE_PATH

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")  # ✅ Enforce foreign keys
    return conn