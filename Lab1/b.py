# s = str(input())
# q = 0
# for i in s:
#     a = ord(i)
#     q += a
# if q > 300:
#     print('It is tasty!')
# else:
#     print('Oh, no!')

s = str(input())
a = 0
for foods in range(0, len(s)):
    a += ord(s[foods])
if a > 300:
    print('It is tasty!')
else:
    print('Oh, no!')