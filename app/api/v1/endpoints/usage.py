from fastapi import APIRouter, Depends
from app.models.usage_model import UsageLogOut
from app.core.dependencies import get_current_user

router = APIRouter()

@router.get("/usage", response_model=list[UsageLogOut])
async def get_usage(current_user=Depends(get_current_user)):
    # DB query here
    return []