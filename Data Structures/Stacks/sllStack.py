"""
Stack implementation using singly linked list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class sllStack:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    
    """
    Helper methods
    """
    def size(self):
        return print(f'Size of stack: {self.size}')

    def peek(self):
        return print(f'Current HEAD: {self.head.value}')
    
    def isEmpty(self):
        if self.__isEmpty():
            return print("Empty stack")
        
        return print("NOT Empty stack")

    def __isEmpty(self):
        if self.size == 0:
            return True
        
        return False
    """
    Push
    """
    def push(self, node):
        node.next = self.head
        self.head = node 

        self.size += 1
    """
    Pop
    """
    def pop(self):
        if self.__isEmpty():
            return print(RuntimeError("Empty Stack"))
        
        # Assign temporary pointer to self.head neighbor
        current = self.head.next
        
        # Deallocate
        self.head.next = None

        # Assign new head
        self.head = current 

        self.size -= 1
    """
    Print
    """
    def print(self):
        current = self.head

        while current:
            print(f'{current.value}',end="->")
            current = current.next
        print("None")
        print()

node = sllStack()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

node.push(e1)
node.push(e2)
node.push(e3)
node.pop()
node.push(e4)
node.pop()
node.pop()
node.pop()
node.pop()
node.pop()
node.pop()
node.pop()
node.push(e1)
node.push(e2)
node.push(e3)
node.peek()


node.print()