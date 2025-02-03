def isBalanced(s):
    arr = []
    brackets = {'{':'}', '[':']', '(':')'}
    for char in s:
        if char in ['{', '[', '(']:
            arr.append(char)
        else:
            if arr:
                top = arr.pop()
                if brackets[top] != char:
                    return 'No'
            else:
                return 'No'
    return 'No' if arr else 'Yes'


s = str(input()) 
print(isBalanced(s))