# UpperCamelCase
# dunder - double underscore - магические методы

class Animal:

    def __init__(self, my_name, leg_cnt=4):
        self.name = my_name
        self.leg_cnt = leg_cnt

    def __str__(self):
        return self.name + " наш Animal"


dog = Animal(my_name="Aktos")
cat = Animal(my_name="Musya")
monkey = Animal(my_name="Monkey", leg_cnt=2)

print(type(dog))
print(dog.leg_cnt)
print(dog.name)


print(type(cat))
print(cat.leg_cnt)
print(cat.name)

print(type(monkey))
print(monkey.leg_cnt)
print(monkey.name)
