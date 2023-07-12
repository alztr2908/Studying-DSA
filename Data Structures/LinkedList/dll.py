"""
Java Code converted to Python code 
source: https://github.com/williamfiset/DEPRECATED-data-structures/blob/master/com/williamfiset/datastructures/linkedlist/DoublyLinkedList.java
"""

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

    def size(self):
        return self.size

    def isEmpty(self):
        return self.len() == 0

    """
    Append
    """

    """
    Delete
    """

    
    """
    Print
    """