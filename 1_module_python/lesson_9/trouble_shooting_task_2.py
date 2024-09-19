# range( len(a) ) - (0, 1, 2, 3, 4)
# range( 1, len(a) ) - (1, 2, 3, 4)
# range( 0, len(a), 2 ) - (0, 2, 4)
# range( len(a) - 1, -1, -1 ) - (4, 3, 2, 1, 0)

# debug

a = [6, 66, 69, 99, 9]
#    0  1    2   3  4

mx = a[-1]
for i in range(len(a)-1, -1, -1):  # (4, 3, 2, 1, 0)
    print(a[i])

    if mx < a[i]:
        mx = a[i]

print(mx)


