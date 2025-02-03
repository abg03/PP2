n = int(input())
a = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = i*i
        a[i][0] = i
        a[0][j] = j


for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()