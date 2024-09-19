
def custom_filter(func, l):
    result = []
    for elem in l:
        if func(elem):
            result.append(elem)
    return result


def custom_map(func, l):
    result = []
    for elem in l:
        result.append(func(elem))
    return result


a = [1, 4, 77, 12]

# b = list(map(lambda x: x+3, a))
# b = custom_map(lambda x: x+3, a)
# print(b)

# b = list(filter(lambda x: x > 10, a))
b = custom_filter(lambda x: x > 10, a)
print(b)




