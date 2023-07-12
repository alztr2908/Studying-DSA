"""
Java Code converted to Python code 
source: https://github.com/williamfiset/DEPRECATED-data-structures/blob/master/com/williamfiset/datastructures/linkedlist/DoublyLinkedList.java
"""

# Internal node class to represent data
class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = head
        self.tail = None
        self.size = 0
    
    """
    Helper
    """
    # Empty this linked list, O(n)
    def clear(self):
        current = self.head
        while current != None:
            # Assign a temporary reference to hold the next element
            temp = current.next

            # Deallocating the current value
            current.prev = current.next = None
            current.value = None

            # Moving to the next element
            current = temp

        self.head = self.tail = current = None
        self.size = 0

    # Return the size of this linked list
    def size(self):
        return self.size

    # Is this linked list empty?
    def isEmpty(self):
        return self.size == 0

    """
    Append
    """
    # Add an element to the tail of the linked list, O(1)
    def add(self, new_node):
        self.addLast(new_node)
    
    # Add a node to the tail of the linked list, O(1)
    def addLast(self, new_node):
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next 
        
        self.size += 1

    """
    Delete
    """

    
    """
    Print
    """
    def printHEAD(self):
        if not self.head:
            return print(ValueError("No element in HEAD"))
        
        print(f'HEAD: {self.head.value}')

    def printTAIL(self):
        if not self.head:
            return print(ValueError("No element in TAIL"))
        
        print(f'TAIL: {self.tail.value}')

    def print(self):
        self.printHEAD()
        self.printTAIL()

        # Print in ascending order
        print("Print from HEAD to TAIL")
        current = self.head
        while current:
            print(f'{current.value}',end="<=>")
            current = current.next
        print("None")
        print()
        
        # Print in descending order
        print("Print from TAIL to HEAD")
        current = self.tail
        while current:
            print(f'{current.value}',end="<=>")
            current = current.prev
        print("None")
        print()


node = DoublyLinkedList()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

node.add(e2)
node.add(e3)
node.add(e4)
node.print()