s = str(input())
t = input()
d = 0
a = []
for i in s:
    if i == t:
        a.append(d)
    d += 1
if len(a) > 1:
    print(min(a), max(a))
elif len(a) == 1:
    print(max(a))