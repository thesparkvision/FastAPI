from .database import db_connection
from src.config import MAX_COLLECTIONS_COUNT
from uuid import UUID

student_collections = db_connection.db.get_collection("students")

async def get_students():
    query_filter = {}
    return await student_collections.find(query_filter).to_list(length = MAX_COLLECTIONS_COUNT)

async def get_student_by_student_id(student_id: UUID):
    query_filter = {
        'student_id': student_id
    }
    return await student_collections.find_one(query_filter)

async def add_student(student_info: dict):
    return await student_collections.insert_one(student_info)

async def remove_student(student_id: UUID):
    query_filter = {
        'student_id': student_id
    }
    return await student_collections.delete_one(query_filter)

async def update_student(student_id: UUID, student_info: dict):
    query_filter = {
        'student_id': student_id
    }
    return await student_collections.replace_one(query_filter, student_info)