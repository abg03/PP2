n = int(input())
arr = []
for _ in range(n):
    s = input()
    if any(''.join(i).isdigit() for i in s) and \
        any(''.join(i).islower() for i in s) and \
         any(''.join(i).isupper() for i in s):
          arr.append(s)

arr = set(arr)
print(len(arr))
print(*sorted(arr), sep='\n')