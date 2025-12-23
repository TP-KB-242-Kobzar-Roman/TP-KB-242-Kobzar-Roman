from student_List import StudentList

def test_add_student():
    group = StudentList()
    group.add_student("Ivan", "12345")

    assert len(group.students) == 1
    assert group.students[0].name == "Ivan"
    assert group.students[0].phone == "12345"
