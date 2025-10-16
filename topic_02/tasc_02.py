# Створюємо словник
student = {"name": "Roman", "group": "KB-242", "age": 19}
print("Початковий словник:", student)

# update()
student.update({"age": 20, "city": "Kyiv"})
print("Після update():", student)

# keys()
print("Ключі:", list(student.keys()))

# values()
print("Значення:", list(student.values()))

# items()
print("Пари ключ-значення:", list(student.items()))

# del
del student["city"]
print("Після del student['city']:", student)

# clear()
student.clear()
print("Після clear():", student)
