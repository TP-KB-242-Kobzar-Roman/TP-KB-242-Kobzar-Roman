from student_List import StudentList
from file_utils import FileUtils

def main():
    filename = "students.txt"
    group = StudentList()

    # завантаження
    try:
        group.students = FileUtils.load_from_file(filename)
    except:
        pass

    while True:
        print("1 - Показати студентів")
        print("2 - Додати студента")
        print("0 - Вийти")

        choice = input("Вибір: ")

        if choice == "1":
            group.show_students()

        elif choice == "2":
            name = input("Імʼя: ")
            phone = input("Телефон: ")
            group.add_student(name, phone)

        elif choice == "0":
            FileUtils.save_to_file(filename, group.students)
            print("Збережено")
            break

main()
