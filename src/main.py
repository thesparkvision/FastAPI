from fastapi import FastAPI
from src.routes import students
from src.data.database import db_connection

app = FastAPI()
app.include_router(students.router, tags=["Student"], prefix="/students")

@app.on_event("shutdown")
def close_db_connection():
    db_connection.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the App!"}