

class Animal:
    def __init__(self, name: str, leg_cnt: int, color: str):
        self.name = name
        self.leg_cnt = leg_cnt
        self.color = color

    def __str__(self):
        return self.name


class Dog(Animal):

    def __str__(self):
        return self.name + " gav gav"


class Cat(Animal):
    pass


aktos = Dog("Aktos", 4, "Red")
musya = Cat("Musya", 4, "Yellow")

print(aktos)
print(musya)



