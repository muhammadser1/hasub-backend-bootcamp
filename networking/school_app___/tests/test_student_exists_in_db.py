from utils.student_utils.student_exists_in_db import student_exists_in_db


def test_student_exists_in_db():
    ##
    student_id = 1
    result = student_exists_in_db(student_id)
    assert result== True


def test_student_doesnot_exists_in_db():
    ##
    student_id = "15adsas"
    result = student_exists_in_db(student_id)
    assert result == False
