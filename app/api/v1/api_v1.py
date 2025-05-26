from fastapi import APIRouter
from app.api.v1.endpoints import projects, keys, usage, billing, users

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
api_router.include_router(keys.router, prefix="/projects", tags=["Keys"])
api_router.include_router(usage.router, tags=["Usage"])
api_router.include_router(billing.router, tags=["Billing"])