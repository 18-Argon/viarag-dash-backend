from pydantic import BaseModel

class APIKeyOut(BaseModel):
    id: str
    project_id: str
    key: str
    name: str
    is_active: bool
    created_at: str