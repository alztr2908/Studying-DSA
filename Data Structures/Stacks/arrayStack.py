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