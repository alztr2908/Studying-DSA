"""
Res should always be on the stack and be the last element 
result should always be appended on the stack

If element is an operation then get the top 2 elements in stack then calculate it
based on the operation type, store it then append that to stack

stack will always have one element that represents the value so far then return it
hence stack[0]
"""


def evalRPN(tokens: list[str]) -> int:
    stack = []
    op = ["+", "-", "*", "/"]

    # if len(tokens) == 1:
    #     return int(tokens[0])

    for el in tokens:
        if el in op:
            second_el = int(stack.pop())
            first_el = int(stack.pop())
            res = calc(first_el, second_el, el)
            stack.append(res)
        else:
            stack.append(int(el))

    return stack[0]


def calc(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    else:
        return int(a/b)


tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
"""
res = 9+3 = 12
res = 12*-11 = -132
res = 6/-132
"""

tokens2 = ["3", "11", "+", "5", "4", "-", "-"]
tokens2 = ["3"]
print(evalRPN(tokens))
print(evalRPN(tokens2))
# print(int(6/-132))

"""
Wrong solution, result should be inside the stack as an element 
so that flags are not needed, it just increases the complexity.
"""
