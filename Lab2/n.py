arr = []
while True:
    n = int(input())
    arr.append(n)
    if n == 0:
        break
for i in range(len(arr)-1):
    if (len(arr)-1) % 2 == 0:
        if i == len(arr)//2:
            break
        else:
            print(arr[i] + arr[len(arr) - 2 - i], end=' ')
    else:
        if i == (len(arr) // 2) - 1:
            print(arr[i])
            break
        else:
            print(arr[i] + arr[len(arr) - 2 - i], end=' ')

