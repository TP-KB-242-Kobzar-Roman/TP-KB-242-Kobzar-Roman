# lab_01.py

# Список студентів (вже відсортований за ім'ям)
students = [
    {"name": "Bob", "phone": "0631234567", "group": "KB-241", "email": "bob@mail.com"},
    {"name": "Emma", "phone": "0631234567", "group": "KB-242", "email": "emma@mail.com"},
    {"name": "Jon", "phone": "0631234567", "group": "KB-242", "email": "jon@mail.com"},
    {"name": "Zak", "phone": "0631234567", "group": "KB-243", "email": "zak@mail.com"}
]

# --- Друк списку студентів ---
def printAllList():
    print("\n--- Поточний довідник студентів ---")
    for s in students:
        print(f"Name: {s['name']}, Phone: {s['phone']}, Group: {s['group']}, Email: {s['email']}")
    print("------------------------------------")

# --- Додавання нового студента ---
def addNewElement():
    print("\n--- Додавання нового студента ---")
    name = input("Введіть ім'я: ").strip()
    phone = input("Введіть телефон: ").strip()
    group = input("Введіть групу: ").strip()
    email = input("Введіть email: ").strip()

    new_student = {"name": name, "phone": phone, "group": group, "email": email}

    # Знаходимо позицію для вставки, щоб зберегти сортування
    insert_pos = 0
    for s in students:
        if name.lower() > s["name"].lower():
            insert_pos += 1
        else:
            break

    students.insert(insert_pos, new_student)
    print(f" Студента {name} додано.")

# --- Видалення студента ---
def deleteElement():
    print("\n--- Видалення студента ---")
    name = input("Введіть ім'я студента для видалення: ").strip()
    for i, s in enumerate(students):
        if s["name"].lower() == name.lower():
            del students[i]
            print(f" Студента {name} видалено.")
            return
    print(f" Студента {name} не знайдено.")

# --- Оновлення даних студента ---
def updateElement():
    print("\n--- Зміна інформації про студента ---")
    name = input("Введіть ім'я студента для оновлення: ").strip()

    for i, s in enumerate(students):
        if s["name"].lower() == name.lower():
            print(f"Знайдено студента: {s['name']}, {s['phone']}, {s['group']}, {s['email']}")
            print("Введіть нові дані (натисніть Enter, щоб залишити без змін):")

            new_name = input(f"Нове ім'я [{s['name']}]: ").strip()
            new_phone = input(f"Новий телефон [{s['phone']}]: ").strip()
            new_group = input(f"Нова група [{s['group']}]: ").strip()
            new_email = input(f"Новий email [{s['email']}]: ").strip()

            # Оновлюємо поля, якщо введено нові значення
            if new_name != "":
                s["name"] = new_name
            if new_phone != "":
                s["phone"] = new_phone
            if new_group != "":
                s["group"] = new_group
            if new_email != "":
                s["email"] = new_email

            # Видаляємо та вставляємо знову, щоб зберегти сортування
            updated_student = s
            del students[i]

            insert_pos = 0
            for st in students:
                if updated_student["name"].lower() > st["name"].lower():
                    insert_pos += 1
                else:
                    break
            students.insert(insert_pos, updated_student)

            print(" Інформацію про студента оновлено.")
            return

    print(f" Студента {name} не знайдено.")

# --- Основне меню ---
def main():
    while True:
        choice = input("\nВиберіть дію [C - створити, U - оновити, D - видалити, P - друк, X - вихід]: ").strip().upper()
        match choice:
            case "C":
                addNewElement()
                printAllList()
            case "U":
                updateElement()
                printAllList()
            case "D":
                deleteElement()
                printAllList()
            case "P":
                printAllList()
            case "X":
                print("\n Вихід з програми...")
                break
            case _:
                print(" Невірний вибір, спробуйте ще раз.")

main()
