# student_utils.py

import json
from fastapi import Request
from models.student import Student


async def parse_student_from_request(request: Request) -> Student:
    """
    Parse student data from request body and create a Student object.

    Parameters:
        request (Request): The request object containing the student data.

    Returns:
        Student: The parsed Student object.
    """
    body = await request.body()
    body_str = body.decode('utf-8')
    student_data = json.loads(body_str)
    student = Student(**student_data)
    return student
