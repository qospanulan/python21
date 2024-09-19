# • Балл 90 и выше: A
# • Балл 80-89: B
# • Балл 70-79: C
# • Балл 60-69: D
# • Балл меньше 60: F

n = int(input("Балл студента: "))  # n = 76

if n >= 90:  # 76 >= 90 ? False
    print("Ваша оценка: A")
elif n >= 80:  # 76 >= 80 ? False
    print("Ваша оценка: B")
elif n >= 70:  # 76 >= 70 ? True
    print("Ваша оценка: C")
elif n >= 60:
    print("Ваша оценка: D")
else:
    print("Ваша оценка: F")


# if n >= 90:
#     print("Ваша оценка: A")
# elif n <= 89 and n >= 80:   # 89
#     print("Ваша оценка: B")
# elif n <= 79 and n >= 70:
#     print("Ваша оценка: C")
# elif n <= 69 and n >= 60:
#     print("Ваша оценка: D")
# else:
#     print("Ваша оценка: F")


