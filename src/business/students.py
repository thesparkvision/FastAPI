from fastapi import HTTPException, status
from src.data import students
from src.models import students as student_models
from uuid import UUID
import datetime

async def get_all_students():
    student_records = await students.get_students()

    result = {
        "students": student_records,
        "count": len(student_records)
    }

    return result

async def get_student(student_id: UUID):
    student = await students.get_student_by_student_id(student_id)
    
    if not student:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail =  "Student with this Student ID is not present"
        )
    
    return student

async def add_student(student: student_models.Student):
    student_info = dict(student)
    student_info['birth_date'] = datetime.datetime.combine(student.birth_date, datetime.time.min)

    db_response = await students.add_student(student_info)
    if not db_response or not db_response.inserted_id:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail =  "Error in Adding Student"
        )

    return student.student_id
    

async def remove_student(student_id: UUID):
    student = await students.get_student_by_student_id(student_id)
    if not student:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail =  "Student with this Student ID is not present"
        )

    db_response = await students.remove_student(student_id)
    if not db_response or db_response.deleted_count == 0:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail =  "Error in Removing Student"
        )

    return None

async def update_student(student_id: UUID, updated_student: student_models.Student):
    student = await students.get_student_by_student_id(student_id)
    if not student:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail =  "Student with this Student ID is not present"
        )

    student_info = dict(updated_student)
    student_info['student_id'] = student['student_id']
    student_info['birth_date'] = datetime.datetime.combine(student_info['birth_date'], datetime.time.min)

    db_response = await students.update_student(student_id, student_info)
    if not db_response or db_response.modified_count != 1:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail =  "Error in Updating Student"
        )

    return student_info