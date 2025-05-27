from pydantic import BaseModel

class UsageLogCreate(BaseModel):
    api_key_id: str
    project_id: str
    endpoint: str
    token_type: str
    tokens_used: int
    success: bool

class UsageLogOut(BaseModel):
    id: int
    api_key_id: str
    project_id: str
    endpoint: str
    token_type: str
    price_per_1k: float
    tokens_used: int
    success: bool
    timestamp: str