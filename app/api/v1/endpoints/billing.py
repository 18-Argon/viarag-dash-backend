from fastapi import APIRouter, Query, Depends, HTTPException
from app.models.billing_model import BillingSummary
from app.core.pricing import compute_price
from app.core.dependencies import get_current_user

router = APIRouter()


@router.get("/billing", response_model=BillingSummary)
async def get_billing(
        project_id: str = Query(...),
        current_user=Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    user_id = current_user["user_id"]

    # TODO: Verify project belongs to user_id
    total_tokens = 123456  # Replace with DB query filtering by user_id + project_id
    return {
        "project_id": project_id,
        "total_tokens": total_tokens,
        "total_cost": compute_price(total_tokens)
    }
