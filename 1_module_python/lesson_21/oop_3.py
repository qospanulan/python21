# Parent class
# Child class

class Animal:

    def __init__(self, name, leg_cnt):
        self.name = name
        self.leg_cnt = leg_cnt

    def say_something(self):
        print("rrrrrrr")

    def __str__(self):
        return "Животное: " + self.name


class Dog(Animal):

    def __init__(self, name, leg_cnt, dlina_nosa):
        super().__init__(name, leg_cnt)
        self.dlina_nosa = dlina_nosa

    def say_something(self):
        print("aw-aw-aw")

    def __str__(self):
        s = super().__str__()
        return s + ", dlina_nosa: " + str(self.dlina_nosa)


class Cat(Animal):

    def say_something(self):
        print("meow-meow")


class Wolf(Animal):
    pass


aktos = Dog(name="Aktos", leg_cnt=4, dlina_nosa=8)
musya = Cat(name="Musya", leg_cnt=4)
volcan = Wolf(name="cc", leg_cnt=7)

print(volcan)
volcan.say_something()

print(aktos)
aktos.say_something()

print(musya)
musya.say_something()

