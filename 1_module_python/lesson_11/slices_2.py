
l = [12, "Hello", 34, 66, "Justcode", 9]
#     0    1       2   3       4      5
#    -6   -5      -4  -3      -2     -1


# new_l = l[1:-2]
new_l = l[::2]
print(new_l)  # range(0, 3) -> (0, 1, 2)
print(l)
