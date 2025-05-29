CREATE TABLE IF NOT EXISTS usage_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api_key_id TEXT NOT NULL,
    project_id TEXT NOT NULL,
    endpoint TEXT NOT NULL,
    token_type TEXT,
    tokens_used INTEGER NOT NULL,
    price_per_1k REAL NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(api_key_id) REFERENCES api_keys(key),
    FOREIGN KEY(project_id) REFERENCES projects(id)
);