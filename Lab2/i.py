n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    book = input().split()
    if book[0] == '1':
        arr1.append(book[1])
    else:
        if len(arr1) == 0:
            pass
        else:
            arr2.append(arr1.pop(0))
print(*arr2)