# def BinaryToDecimal(binary):
#     decimal, i, dec = 0, 0, 0
#     while binary != 0:
#         dec = binary % 10
#         decimal += dec * pow(2, i)
#         i += 1
#         binary //= 10
#     print(decimal)
# if _name_ == '_main_':
#     b = int(input())
#     print(BinaryToDecimal(b))
# a = int(input())
# print(BinaryToDecimal(a))


binary = int(input())
decimal, i, dec = 0, 0, 0
while binary != 0:
    dec = binary % 10
    decimal += dec*pow(2, i)
    i += 1
    binary //= 10
print(decimal)


# def binaryToDecimal(n):
#     return int(n, 2)
#
#
# # Driver code
# b = input()
# if _name_ == '_main_':
#     print(binaryToDecimal(b))
