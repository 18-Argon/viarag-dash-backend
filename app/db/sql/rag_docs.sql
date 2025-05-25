CREATE TABLE IF NOT EXISTS rag_docs (
    id TEXT PRIMARY KEY,
    api_key_id TEXT,
    collection_name TEXT,
    doc_id TEXT,
    content TEXT,
    metadata TEXT,
    embedded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(api_key_id) REFERENCES api_keys(id)
);