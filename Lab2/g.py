n = int(input())
dict = {}

for _ in range(n):
    name, b = input().split()
    dict[b] = dict.get(b, 0) + 1
    # print(*dict.items(), end='\n')
    # if b not in dict.keys():
    #     dict[b] = 1
    # else:
    #     dict[b] += 1

n = int(input())
for _ in range(n):
    name, b, c = input().split()
    if b in dict.keys():
        dict[b] -= int(c)

demons_left = sum([i for i in dict.values() if i > 0])
print(f'Demons left: {demons_left}')
