from fastapi import APIRouter, Depends, Query, HTTPException
from app.core.dependencies import get_current_user
from app.services import billing_service, project_service

router = APIRouter()

@router.get("/billing/summary")
def billing_summary(project_id: str = Query(...), current_user=Depends(get_current_user)):
    user_projects = project_service.get_user_projects(current_user["user_id"])
    if not any(p.id == project_id for p in user_projects):
        raise HTTPException(status_code=403, detail="Unauthorized project access")
    return billing_service.get_billing_summary(project_id)

@router.get("/billing/by-day")
def billing_by_day(project_id: str = Query(...), current_user=Depends(get_current_user)):
    user_projects = project_service.get_user_projects(current_user["user_id"])
    if not any(p.id == project_id for p in user_projects):
        raise HTTPException(status_code=403, detail="Unauthorized project access")
    return billing_service.get_billing_by_day(project_id)

@router.get("/billing/by-model")
def billing_by_model(project_id: str = Query(...), current_user=Depends(get_current_user)):
    user_projects = project_service.get_user_projects(current_user["user_id"])
    if not any(p.id == project_id for p in user_projects):
        raise HTTPException(status_code=403, detail="Unauthorized project access")
    return billing_service.get_billing_by_token_type(project_id)

@router.get("/billing/by-endpoint")
def billing_by_endpoint(project_id: str = Query(...), current_user=Depends(get_current_user)):
    user_projects = project_service.get_user_projects(current_user["user_id"])
    if not any(p.id == project_id for p in user_projects):
        raise HTTPException(status_code=403, detail="Unauthorized project access")
    return billing_service.get_billing_by_endpoint(project_id)
