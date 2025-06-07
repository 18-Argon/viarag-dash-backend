import os
import app.db.init_db as init_db
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = "./db/viarag.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_PATH}")
INTERNAL_BILLING_SECRET = os.getenv("INTERNAL_BILLING_SECRET", "<KEY>")

def initialize_db():
    if not os.path.exists(DATABASE_PATH):
        print("🆕 Database not found. Initializing schema...")
        init_db.initialize(DATABASE_PATH)
    else:
        print("✅ Database already exists. Skipping initialization.")
