class arrayStack:
    def __init__(self, head=None):
        self.stack = []
        self.head = head
    
    """
    Helper methods
    """
    def size(self):
        return print(f'Size of stack: {len(self.stack)}')
    
    def peek(self):
        return print(f'Current HEAD: {self.head}')
    
    def __isEmpty(self):
        if len(self.stack) == 0:
            return True
        
        return False
    
    def isEmpty(self):
        if self.__isEmpty():
            return print("Empty stack")

        return print("NOT empty stack")
    
    """
    Push
    """
    def push(self, value):
        self.stack.append(value)
        self.head = value

    """
    Pop
    """
    def pop(self):
        if self.__isEmpty():
            return print(RuntimeError("Empty stack"))
        
        self.stack.pop()
        self.head = self.stack[-1]

    """
    Print
    """
    def print(self):
        return print(f'Stack: {self.stack}')

node = arrayStack()

node.push(1)
node.push(2)
node.push(3)
node.push(4)
node.pop()

node.print()
node.peek()