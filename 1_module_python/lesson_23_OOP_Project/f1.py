

class Table:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):  # other is Table object

        if self.z != other.z:
            print("Столы не подходят друг другу!!!")
            return None

        length_sum = self.x + other.x
        new_table = Table(x=length_sum, y=self.y, z=self.z)

        return new_table

    def __gt__(self, other):
        area1 = self.x * self.y
        area2 = other.x * other.y
        result = area1 > area2
        return result

    def __str__(self):
        return f"Длина: {self.x}, Ширина: {self.y}, Высота: {self.z}"


table1 = Table(x=16, y=10, z=30)
table2 = Table(x=15, y=10, z=40)

table = table1 + table2
print(type(table))
print(table)

if table1 > table2:
    print("table1 больше")
else:
    print("table1 не больше")

