from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, name, phone):
        self.students.append(Student(name, phone))

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def show_students(self):
        for student in self.students:
            print(student)
