a = list(map(int, input().split()))
arr = []
if len(a) == 1:
    i = int(input())
    for j in range(a[0]):
        arr.append(i + 2 * j)
    cnt = 0
    for i in arr:
        cnt ^= i
    print(cnt)
else:
    for i in range(a[0]):
        arr.append(a[1] + 2 * i)
    cnt = 0
    for i in arr:
        cnt ^= i
    print(cnt)
