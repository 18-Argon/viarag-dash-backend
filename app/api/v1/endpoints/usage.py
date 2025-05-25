from fastapi import APIRouter
from app.models.usage_model import UsageLogOut

router = APIRouter()

@router.get("/usage", response_model=list[UsageLogOut])
def get_usage():
    # DB query here
    return []