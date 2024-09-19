

class Person:

    def __init__(self, my_name="", my_age=0):  # конструктор
        self.name = my_name
        self.age = my_age


person_1 = Person(my_name="Kairat", my_age=24)
person_2 = Person("Madina", 19)
person_3 = Person()


print(person_1.name, person_1.age)
print(person_2.name)


