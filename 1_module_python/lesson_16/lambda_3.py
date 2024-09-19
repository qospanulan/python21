

def print_type(func):
    print("elem:", func)
    print("тип:", type(func))

    result = func(4, 5)
    print("result:", result)

# x = "hello world"
# x = lambda a, b: a + b


print_type(lambda a, b: a + b)
















# def get_sum(a, b):
#     return a + b
#
#
# print(type(get_sum))
# print(get_sum)
