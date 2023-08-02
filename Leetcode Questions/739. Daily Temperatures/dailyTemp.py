"""
Implements a monotonic stack where elements in the stack is 
appended if last element in stack is greater (ascending) or lesser 
(descending).. that's why the stack is still sorted

if stack is not empty and last element in temperature is greater than
last element in stack, then the stack is just growing

on the other hand, stack_idx tracks the current index and if it reaches a greater
element then it will be subtracted to the current index
"""


def dailyTemp(temperatures):
    stack = []
    stack_idx = []
    answer = [0]*len(temperatures)

    for i in range(len(temperatures)):
        # print(i)
        # print(temperatures[i])
        # print(stack)
        # print(stack_idx)
        # print(stack_idx)

        while stack and stack[-1] < temperatures[i]:
            stack.pop()
            idx = stack_idx.pop()
            ans_idx = i - idx
            # print(f'ans: {ans_idx}')
            answer[idx] += ans_idx

        stack.append(temperatures[i])
        stack_idx.append(i)
        # print(answer)
        # print(stack)
        # print(stack_idx)
        # print()

    return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# output = [1, 1, 4, 2, 1, 1, 0, 0]
print(dailyTemp(temperatures))


"""
answer = [0,0,0,0,0,0,0,0]
stack = [73]

stack_idx = []

if stack[-1] < temp[i]
    dequeue()
    pop()
    stack.append(temp[i])
    queue((i))
"""
