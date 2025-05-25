from fastapi import FastAPI
from app.api.v1.endpoints import projects, keys, usage, billing

app = FastAPI()

app.include_router(projects.router, prefix="/dashboard/projects", tags=["projects"])
app.include_router(keys.router, prefix="/dashboard/projects", tags=["keys"])
app.include_router(usage.router, prefix="/dashboard", tags=["usage"])
app.include_router(billing.router, prefix="/dashboard", tags=["billing"])