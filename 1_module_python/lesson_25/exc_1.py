
print("Начало...")

a = "Hello"
# a = "123"


try:  # попытка
    print("test1")
    print("test2")
    a_int = int(a)
    print("test3")
except Exception as error:
    a_int = 0
    print(f"Error: {error}")
else:
    print("Не было ошибок!")
finally:
    print("Выходим из try-except")

print(f"a_int: {a_int}")
print("Конец!")

