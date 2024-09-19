# *args = arguments
# **kwargs = keyword arguments

def get_sum(a, b, *args):
    # print(type(args))

    print("a:", a)
    print("b:", b)
    print("args:", args)

    s = a + b
    for elem in args:
        s = s + elem

    return s


result = get_sum(12, 5, 7, 99, 8, 23)
print("result:", result)

# result = get_sum()
# print("result:", result)

