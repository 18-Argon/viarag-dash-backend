import os
from app.db.session import get_connection

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "sql")

def run_sql_file(conn, filepath):
    with open(filepath, "r") as f:
        sql = f.read()
    conn.executescript(sql)

if __name__ == "__main__":
    conn = get_connection()
    for sql_file in ["users.sql", "projects.sql", "api_keys.sql", "usage_logs.sql", "rag_docs.sql"]:
        run_sql_file(conn, os.path.join(SCHEMA_DIR, sql_file))
    conn.commit()
    conn.close()
    print("Database initialized.")