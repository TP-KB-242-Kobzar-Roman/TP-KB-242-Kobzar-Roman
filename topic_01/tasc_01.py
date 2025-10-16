# Функції для кожної операції
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ділення на нуль неможливе!"

# Основна програма
print("Оберіть операцію: +, -, *, /")
op = input("Введіть операцію: ")

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if op == '+':
    print("Результат:", add(a, b))
elif op == '-':
    print("Результат:", subtract(a, b))
elif op == '*':
    print("Результат:", multiply(a, b))
elif op == '/':
    print("Результат:", divide(a, b))
else:
    print("Невідома операція!")
