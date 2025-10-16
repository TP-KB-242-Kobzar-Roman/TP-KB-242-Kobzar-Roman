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

match op:
    case '+':
        print("Результат:", add(a, b))
    case '-':
        print("Результат:", subtract(a, b))
    case '*':
        print("Результат:", multiply(a, b))
    case '/':
        print("Результат:", divide(a, b))
    case _:
        print("Невідома операція!")
