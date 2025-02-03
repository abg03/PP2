s = int(input())
t = '@gmail.com'
for i in range(s):
    i = str(input())
    if '@gmail.com' in i:
        print(i.replace('@gmail.com', ' '))
    else:
        continue