from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from app import config
from app.db import init_db
from app.logging import get_logger
from app.main import app


@pytest.fixture(
    params=[
        pytest.param(
            ("asyncio", {"use_uvloop": True}),
            id="asyncio+uvloop",
        ),
    ]
)
def anyio_backend(request):
    return request.param


@pytest.fixture
async def client() -> AsyncGenerator:
    async with AsyncClient(
        app=app,
        base_url="http://testserver",
    ) as client:
        app.state.logger = get_logger(__name__)
        init_db(
            database=config.TEST_MONGO_DB,
            app_global_state=app.state,
        )
        yield client
