from sys import argv
from phonebook import load_students, add_student, save_students

def main():
    filename = argv[1]
    students = load_students(filename)

    while True:
        print("1 - Показати")
        print("2 - Додати")
        print("0 - Вийти")

        choice = input("Вибір: ")

        if choice == "1":
            for s in students:
                print(s["Name"], "-", s["Phone"])

        elif choice == "2":
            name = input("Імʼя: ")
            phone = input("Телефон: ")
            add_student(students, name, phone)

        elif choice == "0":
            save_students(filename, students)
            print("Збережено")
            break

main()
