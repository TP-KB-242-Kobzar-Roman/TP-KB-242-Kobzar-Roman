from phonebook import add_student

def test_add_student():
    students = []
    add_student(students, "Ivan", "12345")
    assert len(students) == 1
    assert students[0]["Name"] == "Ivan"
    assert students[0]["Phone"] == "12345"
