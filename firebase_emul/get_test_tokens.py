import requests

FIREBASE_AUTH_EMULATOR_HOST = "http://localhost:9099"
EMAIL = "test@example.com"
PASSWORD = "password123"

def get_id_token(email, password):
    url = f"{FIREBASE_AUTH_EMULATOR_HOST}/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=fake-api-key"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    resp = requests.post(url, json=payload)
    if resp.status_code != 200:
        print("❌ Login failed:", resp.json())
        return None

    data = resp.json()
    print("✅ JWT (idToken):\n")
    print(data["idToken"])
    print("\n📌 Use this in Authorization header as:\nBearer " + data["idToken"])
    return data["idToken"]

if __name__ == "__main__":
    get_id_token(EMAIL, PASSWORD)
