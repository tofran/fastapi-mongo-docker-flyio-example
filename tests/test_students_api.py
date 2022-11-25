import pytest
from bson import ObjectId
from fastapi import status
from httpx import AsyncClient

pytestmark = pytest.mark.anyio


@pytest.mark.parametrize(
    "payload, status_code",
    (
        (
            {"name": "Sample student name"},
            status.HTTP_201_CREATED,
        ),
    ),
)

async def test_add_document(client: AsyncClient, payload: dict, status_code: int):
    response = await client.post("/api/students", json=payload)
    assert response.status_code == status_code
    assert ObjectId.is_valid(response.json()["id"])
