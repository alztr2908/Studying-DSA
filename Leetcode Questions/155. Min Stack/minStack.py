"""
self.min acts as a stack also
it updates if val <= last element of self.min

if the popped element is equal to last element of self.min
self.min gets pop also.. essentially a stack!
"""


class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        if len(self.min) == 0:
            self.min.append(val)
            return None

        if val <= self.min[-1]:
            self.min.append(val)

        return None

    def pop(self) -> None:
        last_val = self.arr.pop()

        if last_val == self.min[-1]:
            self.min.pop()
        return None

    def top(self) -> int:
        if len(self.arr) == 0:
            return None

        return self.arr[-1]

    def getMin(self) -> int:
        if self.min == 0:
            return None

        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
