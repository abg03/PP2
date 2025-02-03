a = map(str, input().split())
for i in a:
    if len(i) >= 3:
        print(i, end=' ')
    else:
        continue