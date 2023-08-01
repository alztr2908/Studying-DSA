def evalRPN(tokens: list[str]) -> int:
    stack = []
    first_op_flag = 1  # since stack takes two elements on first operation
    postfix_flag = 0
    op = ["+", "-", "*", "/"]
    for el in tokens:
        # print(stack)
        if el in op:
            if first_op_flag:
                # b comes first because it was the last element
                b = int(stack.pop())
                a = int(stack.pop())
                res = calc(a, b, el)
                first_op_flag = 0
            else:
                b = int(stack.pop())
                if postfix_flag:
                    res = calc(res, b, el)
                    postfix_flag = 0
                else:
                    res = calc(b, res, el)
            if len(stack) == 0:
                postfix_flag = 1

            # print(res)
        else:
            stack.append(el)

    return res


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

tokens2 = ["3", "11", "+", "5", "-"]
print(evalRPN(tokens))
print(evalRPN(tokens2))
# print(int(6/-132))
