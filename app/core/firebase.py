import firebase_admin
from firebase_admin import credentials, auth
import os

cred_path = os.getenv("FIREBASE_CREDENTIAL_PATH", "firebase-admin-key.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def verify_token(id_token: str):
    try:
        return auth.verify_id_token(id_token)
    except Exception:
        return None
