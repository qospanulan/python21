# positional arguments, keyword arguments

def get_sum(a, b):
    print("a:", a)
    print("b:", b)
    return a + b


result = get_sum(b=12, a=5)
print("result:", result)


# result = get_sum(5, 12)
# print("result:", result)
