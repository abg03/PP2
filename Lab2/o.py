dict = {
    'ZER': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOU': 4,
    'FIV': 5,
    'SIX': 6,
    'SEV': 7,
    'EIG': 8,
    'NIN': 9
}


def sum_of_numbers(x):
    num1, num2 = str(x).split('+')
    first_digit = ""
    second_digit = ""

    for i in range(0, len(num1), 3):
        first_digit += str(dict[num1[i:i+3]])
    for i in range(0, len(num2), 3):
        second_digit += str(dict[num2[i:i+3]])

    final_sum = int(first_digit) + int(second_digit)

    final = ""
    for i in str(final_sum):
        final += list(dict.keys())[list(dict.values()).index(int(i))]

    return final


print(sum_of_numbers(input()))
