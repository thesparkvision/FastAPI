from datetime import date
from typing import Annotated, List
from uuid import UUID, uuid4

from fastapi import Query
from pydantic import BaseModel, Field


class Student(BaseModel):
    student_id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    primary_contact: Annotated[str, Query(min_length= 10, max_length=10)]
    secondary_contact: Annotated[str | None, Query(min_length= 10, max_length=10)] = None
    birth_date: date
    address: str

class Students(BaseModel):
    students: List[Student]
    count: int