import os

from app.logging import get_logger

logger = get_logger(__name__)


APP_VERSION: str = os.getenv("APP_VERSION", "0.0.1-development")
MONGO_URL: str = os.getenv("MONGO_URL")
MONGO_DB: str = os.getenv("MONGO_DB")
