def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Ділення на нуль!"

while True:
    print("\nОберіть операцію (+, -, *, /) або введіть 'exit' для виходу")
    op = input("Операція: ")

    if op.lower() == 'exit':
        print("Програма завершена.")
        break

    a = float(input("Перше число: "))
    b = float(input("Друге число: "))

    if op == '+':
        print("Результат:", add(a, b))
    elif op == '-':
        print("Результат:", sub(a, b))
    elif op == '*':
        print("Результат:", mul(a, b))
    elif op == '/':
        print("Результат:", div(a, b))
    else:
        print("Невідома операція!")
