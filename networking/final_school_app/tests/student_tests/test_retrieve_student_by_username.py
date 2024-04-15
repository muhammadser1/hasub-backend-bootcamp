import pytest

from utils.file_operations import write_json
from utils.student_utils.retrieve_student_by_username import retrieve_student_by_username

db_path="data/db_students.json"
data = {
    "1": {"id": 1, "name": "Alice", "age": 20, "classes": ["Math", "Science"]},
    "2": {"id": 2, "name": "Bob", "age": 21, "classes": ["English", "History"]}
}
write_json(data, db_path)


def test_student_exists():
    username = "1"
    result = retrieve_student_by_username(db_path, username)
    assert result["id"]==int(username)

def test_student_not_exists():
    username = "10"
    result = retrieve_student_by_username(db_path, username)
    assert result is None

def test_db_not_found():
    username = "10"
    db_path="file_path"
    assert retrieve_student_by_username(db_path, username) is None
