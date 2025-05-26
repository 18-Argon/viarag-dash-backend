from fastapi import APIRouter, Depends
from app.models.project_model import ProjectCreate, ProjectOut
from app.core.dependencies import get_current_user
from app.services import project_service

router = APIRouter()

@router.post("", response_model=ProjectOut)
async def create_project(project: ProjectCreate, current_user=Depends(get_current_user)):
    user_id = current_user["user_id"]
    return project_service.create_project(user_id=user_id, project=project)

@router.get("", response_model=list[ProjectOut])
async def list_projects(current_user=Depends(get_current_user)):
    user_id = current_user["user_id"]
    return project_service.get_user_projects(user_id)
