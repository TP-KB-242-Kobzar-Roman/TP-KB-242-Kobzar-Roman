from operations import dia, num
from functions import fun
while True:

    w = dia()
    a = num("F")
    b = num("S")

    f = fun(w, a, b)

    print(f)
    print('--------------------')

def fun(w, a, b):
    match w:
        case "+":
            c = a+b
            return c
        case "-":
            c = a-b
            return c
        case "*":
            c = a*b
            return c
        case "/":
            try:
                c = a/b
                return c
            except ZeroDivisionError:
                return "ZeroDivisionError"
        case _:
            return 'Error!'


def dia():
    w = input("Dia: ")
    if w == "ex":
        return 'exit'
    else:
        return w


def num(nomer):
    while True:
        try:
            num = (input(f"{nomer} num: "))
            n = float(num)
            return n
        except ValueError:
            print(f"'{num}': is not integer")
