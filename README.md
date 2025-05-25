# 📊 ViaRAG Dashboard Backend

This is the backend service powering the **ViaRAG developer dashboard**. It provides APIs for:

* 🔐 Managing API keys per project
* 📁 Project creation and deletion
* 📈 Tracking token usage per key/project
* 💳 Calculating billing based on usage
* 🧺 Powering the dashboard UI and dev playground

This backend is designed to work **in tandem with the ViaRAG SaaS API backend** and shares a unified PostgreSQL database.

---

## 🧱 Tech Stack

* **Python** (FastAPI)
* **PostgreSQL** (shared DB with SaaS backend)
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
│   ├── db/
│   │   ├── sql/            # Raw .sql table definitions
│   │   ├── init_db.py      # Load schema into the database
│   │   └── session.py      # DB connection handling
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
DATABASE_URL=postgresql://user:password@localhost:5432/viarag
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python app/db/init_db.py
```

This runs the `.sql` files in `app/db/sql/` to create tables.

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
