n = int(input())
a = [[0 for i in range(n)] for j in range(n)]


if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i >= j:
                a[i][j] = '#'
            else:
                a[i][j] = '.'


else:
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                a[i][j] = '#'
            else:
                a[i][j] = '.'


for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()