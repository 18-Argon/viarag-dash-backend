from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectOut(ProjectCreate):
    id: str
    created_at: str
    description: Optional[str] = None