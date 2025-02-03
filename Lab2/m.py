arr = []
while True:
    s = input()
    if s == '0':
        break
    day, month, year = map(str, s.split())
    arr.append((day, month, year))

for i in sorted(arr, key=lambda x: (x[2], x[1], x[0])):
    print(*i)