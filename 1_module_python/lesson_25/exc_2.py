# a = "Hello"
a = "123"


try:  # попытка
    print("test1")
    a_int = int(a)
    b = 15/0
    print("test2")
except ValueError as error:
    a_int = 0
    b = 0
    print(f"Error: {error}")
except ZeroDivisionError as error:
    b = 0
    print(f"Error: {error}")


print(f"a_int: {a_int}")
print(f"b: {b}")
print("Конец!")

