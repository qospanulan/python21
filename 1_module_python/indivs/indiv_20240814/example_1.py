
class StrangeNumber:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.x = 80

    def get_info(self):
        return f"{self.a} - {self.b}"

    def __str__(self):
        return f"{self.a} - {self.b}"

    def __len__(self):
        return self.a + self.b

    def __eq__(self, other):
        return ...


number1 = StrangeNumber(5, 1)
number2 = StrangeNumber(77, 20)

number2.x = 34


print(number1.x)
print(number2.x)









# a = [1, 4, 5, 7]
# b = 1
# print(len(b))














