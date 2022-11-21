from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

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
        yield client
