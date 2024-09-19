
def get_changed_list(l, func):
    changed_numbers = []
    for elem in l:
        changed_number = func(elem)
        changed_numbers.append(changed_number)

    return changed_numbers
numbers = [7, 3, 12, 6]
print(numbers)
squared_numbers = get_changed_list(numbers, lambda x: x ** 2)
print(squared_numbers)

