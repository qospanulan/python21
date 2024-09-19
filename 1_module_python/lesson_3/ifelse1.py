# +, -, /, *
# PEP8

# ЕСЛИ operator равно '+' то result = number_1 + number_2
# ИНАЧЕ, ЕСЛИ operator равно '-' то result = number_1 - number_2
# ИНАЧЕ, ЕСЛИ operator равно '*' то result = number_1 * number_2
# ИНАЧЕ result = number_1 / number_2

print("Calculator!")

number_1 = int(input("Number 1: "))  # 12
number_2 = int(input("Number 2: "))  # 10
operator = input("Operator: ")       # '-'


if operator == "+":
    print("Мы внутри блока кода if +")
    result = number_1 + number_2
elif operator == "-":
    print("Мы внутри блока кода if -")
    result = number_1 - number_2
elif operator == "*":
    print("Мы внутри блока кода if *")
    result = number_1 * number_2
else:
    print("Мы внутри блока кода if /")
    result = number_1 / number_2

print("Result:", result)

