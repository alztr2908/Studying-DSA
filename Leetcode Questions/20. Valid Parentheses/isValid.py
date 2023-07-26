"""
Solution
    - traverse s if opening parenthesis, keep on stack
    - if closing, check if the top element in stack matches
        - if yes, pop the stack
        - if no return False 
"""


def isValid_me(s: str) -> bool:
    stack = []
    leftSide = {")": "(", "}": "{", "]": "["}
    rightSide = {"(": ")", "{": "}", "[": "]"}

    for par in s:
        if par in rightSide:
            stack.append(par)
        if par in leftSide:
            # early return in testcases like ")()" -> not valid matic
            if len(stack) == 0:
                return False
            if leftSide[par] == stack[-1]:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True


def isValid(s: str) -> bool:
    hash_map = {'{': '}', '(': ')', '[': ']'}
    stack = []
    if len(s) >= 1 and len(s) <= pow(10, 4):
        for i in s:
            if i in hash_map.keys():
                stack.append(i)
            elif len(stack) != 0 and i == hash_map[stack[-1]]:
                stack.pop()
            elif i in hash_map.values():
                return False

    return not bool(stack)


s1 = "()[]{}"
s2 = "(]"
print(isValid(s1))
print(isValid(s2))
