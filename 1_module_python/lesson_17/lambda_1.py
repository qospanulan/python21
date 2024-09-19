

def print_start_and_end(func, arg1, arg2):
    print("Начало выполнения функции!")
    result = func(arg1, arg2)
    print("Функция выполнена!")
    return result


def get_sum(a, b):
    return a + b


def get_pow(a, n):
    return a ** n


result = print_start_and_end(get_sum, 1, 2)
print("result:", result)


result = print_start_and_end(get_pow, 2, 3)
print("result:", result)









# print("Начало выполнения функции!")
# result = get_sum(1, 2)
# print("Функция выполнена!")
# print("result:", result)
#
# print("Начало выполнения функции!")
# result = get_pow(2, 3)
# print("Функция выполнена!")
#
# print("result:", result)





