from fastapi import APIRouter, status
from business import students
from models import students as student_models
from uuid import UUID

router = APIRouter()

@router.get(
    path = "/", 
    response_model = student_models.Students,
    status_code = status.HTTP_200_OK
)
async def get_all_students():
    return await students.get_all_students()

@router.get(
    path = "/{student_id}", 
    response_model=student_models.Student,
    status_code = status.HTTP_200_OK
)
async def get_student(student_id: UUID):
    return await students.get_student(student_id)

@router.delete(
    path = "/{student_id}",
    status_code = status.HTTP_204_NO_CONTENT
)
async def remove_student(student_id: UUID):
    return await students.remove_student(student_id)

@router.post(
    path = "/",
    status_code = status.HTTP_201_CREATED
)
async def add_student(student: student_models.Student):
    return await students.add_student(student)

@router.put(
    path = "/{student_id}",
    status_code = status.HTTP_200_OK
)
async def add_student(student_id: UUID, updated_student: student_models.Student):
    return await students.update_student(student_id, updated_student)