
# dunder = double underscore
# magic

class Person:

    def __init__(self, my_name="", my_age=0):
        self.name = my_name
        self.age = my_age

    def __str__(self):  # print(), str(person_1)
        person_info = "Name: " + self.name + ". Age: " + str(self.age)
        return person_info

    def get_info(our_object):
        person_info = "Name: " + our_object.name + ". Age: " + str(our_object.age)
        print(person_info)


person_1 = Person(my_name="Kairat", my_age=24)
person_2 = Person(my_name="Madina", my_age=19)

# person_1.get_info()  # Person.get_info(person_1)
# person_2.get_info()


print(person_1)

