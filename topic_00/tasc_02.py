def Diskriminant(a, b, c):
    D = b*b - 4*a*c   
    return D

# Запитуємо у користувача коефіцієнти
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

# Обчислюємо дискримінант
D = Diskriminant(a, b, c)
print(D)

