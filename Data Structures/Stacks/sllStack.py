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
    
    """
    Helper methods
    """

    """
    Push
    """
    def push(self, node):
        node.next = self.head
        self.head = node 
    """
    Pop
    """

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

node = SingleLinkedList()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

node.push(e1)
node.push(e2)
node.push(e3)

node.print()