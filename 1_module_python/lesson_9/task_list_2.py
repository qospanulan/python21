
# max: 45
# min: 1
a = [12, 4, 7, 1, 45, 2, 19]
print("список:", a)

min_elem = a[0]

for i in range(1, len(a)):
    print("Текущее минимум:", min_elem)
    print("Текущее число:", a[i])
    if a[i] < min_elem:
        print("Текущее число меньше минимального, значит у нас новый минимум!")
        min_elem = a[i]
    else:
        print("Текущее число больше минимального! Наш минимум не меняется!")
    print("======================================================")


print("min:", min_elem)
