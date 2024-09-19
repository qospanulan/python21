
"""
n = 5

    *        1 - 4 пробела   n - 1 = 4
   * *       2 - 3 пробела   n - 2 = 3
  * * *      3 - 2 пробела   n - 3 = 2
 * * * *     4 - 1 пробел    n - 4 = 1
* * * * *    5 - 0 пробелов  n - 5 = 0

"""

n = 5
for i in range(1, n+1):
    spaces_cnt = n - i
    print(' ' * spaces_cnt, end='')

    for j in range(i):
        print('*', end=' ')
    print()

