import sqlite3
from app.core.config import DATABASE_PATH

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")  # ✅ Enforce foreign keys
    conn.row_factory = sqlite3.Row
    # cursor = conn.execute("PRAGMA foreign_keys")
    # print("FK enforcement is", cursor.fetchone()[0])  # Should print 1
    #
    # print("\n[Foreign Keys in api_keys]")
    # for row in conn.execute("PRAGMA foreign_key_list(api_keys);"):
    #     print(row)
    #
    # print("\n[Foreign Keys in projects]")
    # for row in conn.execute("PRAGMA foreign_key_list(projects);"):
    #     print(row)
    #
    # cursor = conn.execute("PRAGMA foreign_keys")
    # print("FK enforcement is", cursor.fetchone()[0])  # Should print 1

    return conn