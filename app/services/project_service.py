from app.db.session import get_connection
from fastapi import HTTPException
from app.models.project_model import ProjectCreate, ProjectOut
import uuid
import datetime
from typing import List


def create_project(user_id: str, project: ProjectCreate) -> ProjectOut:
    try:
        with get_connection() as db:
            project_id = str(uuid.uuid4())
            created_at = datetime.datetime.utcnow().isoformat()
            db.execute(
                """
                INSERT INTO projects (id, user_id, name, description, created_at)
                VALUES (?, ?, ?, ?, ?);
                """,
                (project_id, user_id, project.name, project.description, created_at)
            )
            return ProjectOut(
                id=project_id,
                name=project.name,
                description=project.description,
                created_at=created_at
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_user_projects(user_id: str) -> List[ProjectOut]:
    with get_connection() as db:
        cur = db.execute(
            "SELECT id, name, description, created_at FROM projects WHERE user_id = ?",
            (user_id,)
        )
        return [
            ProjectOut(
                id=row[0],
                name=row[1],
                description=row[2],
                created_at=row[3]
            ) for row in cur.fetchall()
        ]
