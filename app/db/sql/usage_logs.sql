CREATE TABLE IF NOT EXISTS usage_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api_key_id TEXT,
    project_id TEXT,
    endpoint TEXT NOT NULL,
    model TEXT,
    tokens_used INTEGER NOT NULL,
    success BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(api_key_id) REFERENCES api_keys(id),
    FOREIGN KEY(project_id) REFERENCES projects(id)
);