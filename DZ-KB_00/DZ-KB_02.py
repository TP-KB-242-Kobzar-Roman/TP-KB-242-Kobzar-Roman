import math

# Запитуємо у користувача коефіцієнти
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

# Обчислюємо дискримінант
D = b*b - 4*a*c

# Знаходимо корені
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Два корені: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Один корінь: x = {x}")
else:
    print("Коренів немає")