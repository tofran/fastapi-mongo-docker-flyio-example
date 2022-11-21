from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.db import get_db

router = APIRouter()


@router.get(
    "",
    status_code=HTTP_200_OK,
    response_description="HTTP server is OK",
    description="Simple HTTP server health check."
)
async def http_health_check():
    return "OK"


@router.get(
    "/db",
    status_code=HTTP_200_OK,
    response_description="DB connection is OK",
    description="Checks if the DB is responsive."
)
async def db_health_check():
    result = await get_db().command("dbstats")
    if result["ok"] != 1.0:
        raise RuntimeError(
            f"Mongo returned OK={result['ok']} status for 'dbstats'"
        )

    return "OK"
