from motor.motor_asyncio import AsyncIOMotorClient

from app import config

_APP_GLOBAL_STATE = None


def init_db(
    mongo_url=None,
    database=None,
    app_global_state=None
):
    global _APP_GLOBAL_STATE

    mongo_url = mongo_url or config.MONGO_URL
    database = database or config.MONGO_DB

    mongodb_client = AsyncIOMotorClient(mongo_url)
    mongodb_connection = mongodb_client[database]

    if app_global_state:
        _APP_GLOBAL_STATE = app_global_state
        app_global_state.mongodb_client = mongodb_client
        app_global_state.mongodb_connection = mongodb_connection

    return (mongodb_client, mongodb_connection)


def get_db():
    mongodb_connection = _APP_GLOBAL_STATE.mongodb_connection

    if mongodb_connection is None:
        raise RuntimeWarning("DB not initialized with a global state.")

    return mongodb_connection


def get_collection(collection: str):
    return get_db()[collection]
