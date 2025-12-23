import csv

def load_students(filename):
    students = []
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def add_student(students, name, phone):
    students.append({"Name": name, "Phone": phone})

def save_students(filename, students):
    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone"])
        writer.writeheader()
        writer.writerows(students)
