from models.student_model import Student
from utils.student_utils.update_student import update_student


def test_update_success():
    student = Student(id=1, name="John", age=20, classes=["Math", "Science"])
    result_db = update_student(student)
    assert student.id in result_db
    assert result_db[student.id]["id"] == student.id
    assert result_db[student.id]["name"] == student.name
    assert result_db[student.id]["age"] == student.age
    assert result_db[student.id]["classes"] == student.classes
