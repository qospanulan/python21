

def print_type(elem):
    print("Тип элемента:", type(elem))
    result = elem(4, 5)
    print("result:", result)


def get_sum(a, b):
    return a + b


x = "hello world!"

print_type( get_sum )
# print_type(x)




