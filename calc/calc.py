from operations import dia, num
from functions import function


class Calc:
    def calculator(self, w, a, b):
        if w == '+':
            return function.add(a, b)
        elif w == '-':
            return function.subtract(a, b)
        elif w == '*':
            return function.multiply(a, b)
        elif w == '/':
            return function.divide(a, b)
        else:
            return "Невідома операція"


def main():
    while True:
        w = dia()
        a = num("перше")
        b = num("друге")

        c = Calc()
        result = c.calculator(w, a, b)

        print("Результат:", result)
        print("------------------")


main()
