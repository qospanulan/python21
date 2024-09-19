def get_square(x):
    return x ** 2


def get_cube(x):
    return x ** 3


def get_plus_3(x):
    return x + 3

# def get_plus_3(l):
#     changed_numbers = []
#     for elem in l:
#         changed_number = elem + 3
#         changed_numbers.append(changed_number)
#     return changed_numbers


def get_changed_list(l, func):
    changed_numbers = []
    for elem in l:
        changed_number = func(elem)
        changed_numbers.append(changed_number)

    return changed_numbers


numbers = [7, 3, 12, 6]
squared_numbers = get_changed_list(numbers, get_square)
tripled_numbers = get_changed_list(numbers, get_cube)
plus_3_list = get_changed_list(numbers, get_plus_3)

print(squared_numbers)
print(tripled_numbers)
print(plus_3_list)
