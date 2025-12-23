# пріоритети операторів
priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

# 1. Перетворення інфіксного виразу у ЗПЗ
def infix_to_rpn(expression):
    stack = []
    output = []
    tokens = expression.split()

    for token in tokens:
        # якщо число — у вихід
        if token.isdigit():
            output.append(token)

        # якщо відкриваюча дужка
        elif token == '(':
            stack.append(token)

        # якщо закриваюча дужка
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # прибираємо '('

        # якщо оператор
        else:
            while (stack and stack[-1] != '(' and
                   priority.get(stack[-1], 0) >= priority.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)

    # виштовхуємо все зі стека
    while stack:
        output.append(stack.pop())

    return output


# 2. Обчислення ЗПЗ
def calculate_rpn(rpn):
    stack = []

    for token in rpn:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]


# Головна частина
expression = input("Введіть вираз (через пробіли): ")

rpn = infix_to_rpn(expression)
print("Зворотний польський запис:", " ".join(rpn))

result = calculate_rpn(rpn)
print("Результат:", result)
