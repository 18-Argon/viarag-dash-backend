# 📊 ViaRAG Dashboard Backend

This is the backend service powering the **ViaRAG developer dashboard**. It provides APIs for:

* 🔐 Managing API keys per project
* 📁 Project creation and deletion
* 📈 Tracking token usage per key/project
* 💳 Calculating billing based on usage
* 🧺 Powering the dashboard UI and dev playground

This backend is designed to work **in tandem with the ViaRAG SaaS API backend** and shares a unified SQLite or PostgreSQL database.

---

## 🧱 Tech Stack

* **Python** (FastAPI)
* **SQLite** (default local dev) or **PostgreSQL** (shared prod DB)
* **Raw SQL schema** (no ORM)
* **Pydantic** (for request/response models)
* **Docker**-friendly design

---

## 📂 Project Structure

```
viarag_dashboard_backend/
├── app/
│   ├── api/v1/endpoints/   # FastAPI routes for projects, keys, usage, billing
│   ├── core/               # Config, pricing logic, auth
│   ├── db/                 # SQL schema, DB connection, init
│   ├── schemas/            # Pydantic models
│   ├── services/           # Business logic for all endpoints
│   └── main.py             # FastAPI app entrypoint
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-org/viarag-dashboard-backend.git
cd viarag-dashboard-backend
```

### 2. Setup Environment

```bash
cp .env.example .env
```

Edit your `.env` to include:

```
DATABASE_URL=sqlite:///./viarag.db
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python app/db/init_db.py
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

---

## 🔪 Example Endpoints

| Method | Path                            | Description                 |
| ------ | ------------------------------- | --------------------------- |
| GET    | `/dashboard/projects`           | List user projects          |
| POST   | `/dashboard/projects`           | Create a new project        |
| POST   | `/dashboard/projects/{id}/keys` | Generate an API key         |
| GET    | `/dashboard/usage`              | View token usage            |
| GET    | `/dashboard/billing`            | Get token-to-cost breakdown |

---

## 📦 Future Plans

* 🔄 Stripe integration for real billing
* 📊 Enhanced spike detection + email alerts
* 🧑‍🏫 Team-based project sharing
* 📊 Usage anomaly detection

---

## 📜 License

**Proprietary** – All rights reserved. Contact `admin@viarag.ai` for licensing.

---

## 🔧 Core Code

### `app/core/config.py`

```python
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./viarag.db")
```

### `app/core/pricing.py`

```python
def compute_price(tokens: int, rate_per_1k=0.01) -> float:
    return round((tokens / 1000) * rate_per_1k, 4)
```

### `app/core/security.py`

```python
def validate_api_key(key: str) -> bool:
    # Placeholder logic; connect to DB and validate key
    return True
```

### `app/core/auth.py`

```python
from fastapi import Header, HTTPException

def get_user_from_token(authorization: str = Header(...)):
    # Placeholder: In real setup, verify Firebase or session token
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ", 1)[1]
    # Simulated check
    if token != "test-token":
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    return {"user_id": "user_123", "email": "test@example.com"}
```

### `app/main.py`

```python
from fastapi import FastAPI
from app.api.v1.endpoints import projects, keys, usage, billing

app = FastAPI()

app.include_router(projects.router, prefix="/dashboard/projects", tags=["projects"])
app.include_router(keys.router, prefix="/dashboard/projects", tags=["keys"])
app.include_router(usage.router, prefix="/dashboard", tags=["usage"])
app.include_router(billing.router, prefix="/dashboard", tags=["billing"])
```

### ... (API routes and schemas remain unchanged)

Let me know if you want token-based access applied across all routes or if you'd like to integrate real Firebase auth next.
