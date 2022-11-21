from typing import List

from bson import ObjectId
from pymongo.errors import WriteError

from app.db import get_collection
from app.exceptions import AlreadyExistsHTTPException


async def retrieve_document(collection: str, document_id: str) -> dict:
    filter = {"_id": ObjectId(document_id)}

    document = await get_collection(collection).find_one(filter)

    if document:
        return _pop_document_id(document)
    else:
        raise ValueError(f"No document found for {document_id=} in {collection=}")


async def list_documents(
    collection: str,
    limit,
    skip
) -> List[dict]:
    limit = _default_to(limit, 10)
    skip = _default_to(skip, 0)

    return _pop_document_ids(
        await get_collection(collection)
        .find()
        .skip(skip)
        .to_list(limit)
    )


async def create_document(
    collection: str,
    document: dict,
) -> dict:
    try:
        document = await get_collection(collection).insert_one(document)
        return await retrieve_document(collection, document.inserted_id)
    except WriteError:
        raise AlreadyExistsHTTPException(
            f"Document with {document.inserted_id=} already exists"
        )


def _pop_document_id(document: dict) -> dict:
    """
    Helper to pop mongo's `_id` into `id` in a dict
    """
    document["id"] = document.pop("_id")
    return document


def _pop_document_ids(documents: List[dict]) -> dict:
    """
    Perform `_pop_document_id` for a list.
    """
    return [
        _pop_document_id(document)
        for document in documents
    ]


def _default_to(value, default_value):
    """
    Returns `value` if it is not None, otherwise returns `default_value`.
    """
    return default_value if value is None else value
