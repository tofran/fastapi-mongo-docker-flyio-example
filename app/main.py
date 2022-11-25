from fastapi import FastAPI

from app import config
from app.controllers.health_controller import router as health_router
from app.controllers.student_controller import router as students_router
from app.db import init_db
from app.logging import get_logger

app = FastAPI(
    title="Sample project",
    version=config.APP_VERSION,
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(students_router, prefix="/api/students", tags=["students"])


@app.on_event("startup")
async def startup_event():
    app.state.logger = get_logger(__name__)
    app.state.logger.info("Starting starting...")
    init_db(app_global_state=app.state)


@app.on_event("shutdown")
async def shutdown_event():
    app.state.logger.info("Server stopping.")
