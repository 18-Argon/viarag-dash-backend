from pydantic import BaseModel

class BillingSummary(BaseModel):
    project_id: str
    total_tokens: int
    total_cost: float