import math

# Функція для обчислення дискримінанту
def discriminant(a, b, c):
    return b**2 - 4*a*c

# Функція для пошуку коренів квадратного рівняння
def quadratic_roots(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Два дійсних корені: x₁ = {x1}, x₂ = {x2}")
    elif d == 0:
        x = -b / (2*a)
        print(f"Один дійсний корінь: x = {x}")
    else:
        print("Дійсних коренів немає")

# Приклад виклику
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))
quadratic_roots(a, b, c)
