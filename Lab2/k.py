a = list(map(str, input().split()))
a = set(a)
print(len(a))
l = list(a)
l.sort()

for word in l:
    if word[-1] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        print(word[:-1])
    else:
        print(word)

