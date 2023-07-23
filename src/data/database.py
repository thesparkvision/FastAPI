import os
import logging
import motor.motor_asyncio as motor_package
from src import config

logger = logging.Logger(os.path.basename(__file__))

class DatabaseConnection:    
    def __init__(self):
        self.client = motor_package.AsyncIOMotorClient(
            host = config.MONGO_HOST, 
            port = int(config.MONGO_PORT), 
            timeoutMS = 10,
            uuidRepresentation='standard'
        )
        self.db = self.client.get_database(config.DB_NAME)
        logger.info("Database Connection Created!")

    def close(self):
        self.client.close()
        logger.info("Database Connection Closed!")

db_connection = DatabaseConnection()