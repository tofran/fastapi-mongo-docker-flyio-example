from typing import List

from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from app.exceptions import NotFoundHTTPException
from app.schemas.student import Document, DocumentResponse, ObjectIdField
from app.services.repository import create_document, list_documents, retrieve_document

COLLECTION = "students"
router = APIRouter()


@router.post(
    "",
    status_code=HTTP_201_CREATED,
    description="Create a student.",
    response_model=DocumentResponse,
)
async def create_student(payload: Document):
    try:
        result = await create_document(COLLECTION, jsonable_encoder(payload))
        return result
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))


@router.get(
    "",
    description="List students.",
    response_model=List[DocumentResponse],
)
async def list_students(
    skip: int | None = Query(default=None, min=0),
    limit: int | None = Query(default=10, min=1, max=100),
):
    try:
        return await list_documents(COLLECTION, skip=skip, limit=limit)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))


@router.get(
    "/{student_id}",
    description="Retrieve a student.",
    response_model=DocumentResponse,
)
async def get_student(student_id: ObjectIdField):
    try:
        return await retrieve_document(COLLECTION, student_id)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))
