from fastapi import APIRouter, Query
from app.models.billing_model import BillingSummary
from app.core.pricing import compute_price

router = APIRouter()

@router.get("/billing", response_model=BillingSummary)
def get_billing(project_id: str = Query(...)):
    total_tokens = 123456  # Replace with DB aggregation
    return {
        "project_id": project_id,
        "total_tokens": total_tokens,
        "total_cost": compute_price(total_tokens)
    }