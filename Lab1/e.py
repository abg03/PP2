a, b = map(int, input().split())
target = True
for i in range(2, a):
    if a % i == 0:
        target = False
        break
if target and b % 2 == 0 and a < 500:
    print('Good job!')
else:
    print('Try next time!')
