a = int(input())
z = (input())
if z == 'k':
    b = int(input())
    a = a / 1024
    print(round(a, b))
elif z == 'b':
    a = a * 1024
    print(a)