from student import Student

class FileUtils:
    @staticmethod
    def load_from_file(filename):
        students = []
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                name, phone = line.strip().split(",")
                students.append(Student(name, phone))
        return students

    @staticmethod
    def save_to_file(filename, students):
        with open(filename, "w", encoding="utf-8") as file:
            for s in students:
                file.write(f"{s.name},{s.phone}\n")
