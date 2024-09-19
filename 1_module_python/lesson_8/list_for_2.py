# len() - возвращает длину/размер списка, строки, точнее итерируемых объектов
a = [34, "hello", 78, "Justcode", 11, "qwer"]
#    0,     1,    2,       3,      4
#   -5     -4    -3       -2      -1

list_size = len(a)
print("list size:", list_size)

for i in range(list_size):  # [0, 1, 2, 3, 4] i - index
    print("index", i)
    print(a[i])



