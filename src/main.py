import uvicorn
from fastapi import FastAPI

from config import config
from data.database import db_connection
from routes import students

app = FastAPI()
app.include_router(students.router, tags=["Student"], prefix="/students")

@app.on_event("shutdown")
def close_db_connection():
    db_connection.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the App!"}

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=config.APP_HOST,
        port=config.APP_PORT
    )
