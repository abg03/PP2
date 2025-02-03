def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


arr = []
x1, y1 = map(int, (input().split()))
n = int(input())
for i in range(n):
    x2, y2 = map(int, (input().split()))
    a = dist(x1, y1, x2, y2)
    arr.append((x2, y2, a))
for x2, y2, a in sorted(arr, key=lambda x: x[2]):
    print(x2, y2)