# 5! = 1 * 2 * 3 * 4 * 5 = 120
# n! = 1 * 2 * 3 * ... * (n-1) * n

# Дано число двузначное число a,
# поменять местам цифры используя операторы (%, //).
# Ожидаемый результат: если a = 42, result = 24.

a = 62  # 26
first_digit = a // 10
second_digit = a % 10

# result = str(second_digit) + str(first_digit)
result = (second_digit * 10) + first_digit
print(result)












