import os
# from app.db.session import get_connection
import sqlite3

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "sql")

def run_sql_file(conn, filepath):
    with open(filepath, "r") as f:
        sql = f.read()
    conn.executescript(sql)

def initialize(DATABASE_PATH):
    conn = sqlite3.connect(DATABASE_PATH)
    for sql_file in ["users.sql", "projects.sql", "api_keys.sql", "usage_logs.sql", "rag_docs.sql"]:
        run_sql_file(conn, os.path.join(SCHEMA_DIR, sql_file))
    conn.commit()
    conn.close()
    print("Database initialized.")

# if __name__ == "__main__":
#     initialize()