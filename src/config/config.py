from dotenv import dotenv_values

env_values = dotenv_values()

MONGO_URI = env_values.get("MONGO_URI")
APP_PORT = int(env_values.get("APP_PORT", 8000))
APP_HOST = env_values.get("APP_HOST", "0.0.0.0")

DB_NAME = "library"

MAX_COLLECTIONS_COUNT = 100