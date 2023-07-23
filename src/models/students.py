from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Annotated
from uuid import UUID, uuid4
from datetime import date
from fastapi import Query

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