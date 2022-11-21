from motor.motor_asyncio import AsyncIOMotorClient

from app import config

_MONGODB_CLIENT = None
_MONGODB_CONNECTION = None


def init_db():
    global _MONGODB_CLIENT, _MONGODB_CONNECTION

    _MONGODB_CLIENT = AsyncIOMotorClient(config.MONGO_URL)
    _MONGODB_CONNECTION = _MONGODB_CLIENT[config.MONGO_DB]


def get_db():
    if _MONGODB_CONNECTION is None:
        init_db()

    return _MONGODB_CONNECTION


def get_collection(collection: str):
    return get_db()[collection]
