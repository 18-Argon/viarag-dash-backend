from fastapi import APIRouter, Depends, Query, HTTPException
from app.models.usage_model import UsageLogOut, UsageLogCreate
from app.core.dependencies import get_current_user, require_internal_auth
from app.services import usage_service, project_service

router = APIRouter()

@router.get("/usage", response_model=list[UsageLogOut])
def get_usage(
    project_id: str = Query(...),
    current_user=Depends(get_current_user)
):
    user_projects = project_service.get_user_projects(current_user["user_id"])
    if not any(p.id == project_id for p in user_projects):
        raise HTTPException(status_code=403, detail="Unauthorized project access")

    return usage_service.get_usage_logs(project_id)


@router.get("/usage/internal", response_model=list[UsageLogOut])
def get_usage_internal(
    project_id: str = Query(...),
    auth=Depends(require_internal_auth)
):
    return usage_service.get_usage_logs(project_id)


@router.post("/usage/internal/log")
def log_usage_internal(
    log: UsageLogCreate,
    auth=Depends(require_internal_auth)
):
    return usage_service.log_usage(log)
