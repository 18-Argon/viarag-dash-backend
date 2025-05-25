from pydantic import BaseModel

class UsageLogOut(BaseModel):
    id: int
    api_key_id: str
    project_id: str
    endpoint: str
    model: str
    tokens_used: int
    success: bool
    timestamp: str