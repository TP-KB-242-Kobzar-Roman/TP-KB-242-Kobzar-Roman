# --- Функції операцій ---
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:  #  обертаємо рядок ділення
        return a / b
    except ZeroDivisionError:
        return " Помилка: ділення на нуль!"

# --- Основна програма ---
while True:
    print("\nОберіть операцію: +, -, *, / або 'exit' для виходу")
    op = input("Операція: ")

    if op.lower() == "exit":
        print(" Програма завершена.")
        break

    try:  #  обертаємо рядки, де вводяться числа
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:  # якщо введено не число
        print(" Помилка: введено не число!")
        continue  # повертаємось на початок циклу

    # --- Виконуємо операцію ---
    if op == '+':
        print("Результат:", add(a, b))
    elif op == '-':
        print("Результат:", sub(a, b))
    elif op == '*':
        print("Результат:", mul(a, b))
    elif op == '/':
        print("Результат:", div(a, b))
    else:
        print(" Невідома операція!")
