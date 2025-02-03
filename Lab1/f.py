a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in a:
    if i <= 10:
        print('Go to work!')
    elif i in range(11, 26):
        print('You are weak')
    elif i in range(26, 46):
        print('Okay, fine')
    elif i > 45:
        print('Burn! Burn! Burn Young!')
