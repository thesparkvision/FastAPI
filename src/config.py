from dotenv import dotenv_values
env_values = dotenv_values()

MONGO_HOST = env_values.get("MONGO_HOST")
MONGO_PORT = env_values.get("MONGO_PORT")

DB_NAME = "library"

MAX_COLLECTIONS_COUNT = 100