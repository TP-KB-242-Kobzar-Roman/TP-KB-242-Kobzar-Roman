class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is missing")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            number = int(value)
        except ValueError:
            raise ValueError("It isn't number")

        if number < 0 or number > 110:
            raise ValueError("Errore!")
        self._age = number

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

# ------------------------------------------------------------------

def get_student_list():
    students = []

    while True:
        name = input("Enter name: ")
        if name == 'ex':
            break
        age = (input("Enter age: "))
        print("------------------")

        slovnuk = Student(name, age)
        students.append(slovnuk)

    return students
# ------------------------------------------------------------------

def znch_sort():
    while True:
        m = input("za chum sortuvaty: ")
        if m != "name" and m != "age":
            print("Errore! Try again.")
        else:
            return m

def sort(listochek, namekey):
    for elem in sorted(listochek, key=lambda x: getattr(x, namekey)):
        print(elem)

# ------------------------------------------------------------------

def main():

    spusok = get_student_list()
    c = znch_sort()
    print("------------------")
    sort(spusok, c)

main()
