from random import choice, choices

fruits = ["apple", "banana", "orange"]

# result = choice(fruits)
result = choices(fruits, k=2)
print(result)
