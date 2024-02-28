# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

s = '[([]])'

from collections import deque

brackets = {'(': ')', '[': ']', '{': '}'}

stack = deque()
for i in s:
    if stack:
        temp = stack[len(stack) - 1]
        print(temp)
        print(i)
        if temp in brackets and brackets[temp] == i: 
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)
    print(stack)
if stack:
    print(False)
else:
    print(True)