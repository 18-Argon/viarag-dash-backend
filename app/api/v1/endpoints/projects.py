from fastapi import APIRouter
from app.models.project_model import ProjectCreate, ProjectOut

router = APIRouter()

@router.post("", response_model=ProjectOut)
def create_project(project: ProjectCreate):
    # DB insert logic here
    return {"id": "123", **project.dict(), "created_at": "2025-01-01T00:00:00"}

@router.get("", response_model=list[ProjectOut])
def list_projects():
    # DB fetch logic here
    return []