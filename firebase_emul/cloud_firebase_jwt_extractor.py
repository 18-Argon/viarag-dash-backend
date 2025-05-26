import firebase_admin
from app.core.config import FIREBASE_CREDENTIAL_PATH
from firebase_admin import credentials, auth
import requests

SERVICE_ACCOUNT_PATH = FIREBASE_CREDENTIAL_PATH
API_KEY = "AIzaSyAKxkqo8ex5FCSamC-UndNM65hBt0VSvkI"
USER_UID = "GKaECvUO7ia4lmz9tFbpVlmYYu72"

# Initialize Firebase Admin once
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

# Step 1: Create the custom token (DO NOT decode)
custom_token = auth.create_custom_token(USER_UID)

# Step 2: Exchange it for an ID token
url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={API_KEY}"
payload = {
    "token": custom_token,  # already a str/bytes depending on SDK
    "returnSecureToken": True
}

# Convert to str only if needed
if isinstance(custom_token, bytes):
    payload["token"] = custom_token.decode("utf-8")

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())
print(response.json()['idToken'])