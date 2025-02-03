n = int(input())
d1 = dict()
for i in range(n):
    s = input().split()
    x = s[0]
    y = int(s[1])
    if x not in d1:
        d1[x] = y
    else:
        d1[x] += y
max_number = 0
name = 0
for k, v in sorted(d1.items()):
    if v > max_number:
        max_number = v
        name = k
z = 0
for k, v in sorted(d1.items()):
    z = d1[name] - v
    if z == 0:
        print(k + " is lucky!")
    else:
        print(k + " has to receive " + str(z) + " tenge")

