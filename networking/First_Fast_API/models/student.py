from pydantic import BaseModel
from typing import List


class Student(BaseModel):
    id: int
    name: str
    age: int
    classes: List[str]
