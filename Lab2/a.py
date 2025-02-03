'''
def check(a):
    pos = len(a)-1
    for i in range(len(a) - 2, -1, -1):
        if i + a[i] >= pos:
            pos = i
    return pos == 0


print(check(list(map(int, input().split())))+0)
'''


a = list(map(int, input().split()))
main = len(a)-1
for i in range(len(a)-2, -1, -1):
    if i + a[i] >= main:
        main = i
if main == 0:
    print(1)
else:
    print(0)
# 1 5 2 6 3 4
