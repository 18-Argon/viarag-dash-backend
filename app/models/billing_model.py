from pydantic import BaseModel
from datetime import datetime

class BillingSummary(BaseModel):
    project_id: str
    total_tokens: int
    total_cost: float

class BillingLogResponse(BaseModel):
    status: str
    message: str
    project_id: str
    tokens_used: int
    logged_at: datetime