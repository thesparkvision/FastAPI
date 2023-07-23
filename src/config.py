from dotenv import dotenv_values
env_values = dotenv_values()

MONGO_URI = env_values.get("MONGO_URI")

DB_NAME = "library"

MAX_COLLECTIONS_COUNT = 100