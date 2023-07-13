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
    def len(self):
        return self.size

    # Is this linked list empty?
    def isEmpty(self):
        return self.size == 0

    def indexOf(self, new_node):
        index = 0
        current = self.head

        # Support searching for null
        if new_node is None:
            while current != none:
                if current.data is None:
                    return print(f'Node index: {index}')
                current = current.next
                index += 1
        else:
            while current != None:
                if new_node.value == current.value and new_node.prev == current.prev and new_node.next == current.next:
                    return print(f'Node index of {new_node.value}: {index}')
                current = current.next
                index += 1
        
        return print(f'No index found')

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
            self.tail = new_node
        
        self.size += 1

    # Add an element to the beginning of this linked list, O(1)
    def addFirst(self, new_node):
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
        
    """
    Delete
    """
    # Remove the first value at the head of the linked list, O(1)
    def removeFirst(self):
        # Can't remove data from an empty list
        if self.isEmpty():
            print(RuntimeError("Empty List"))
            return
        
        # Extract the data at the head and move
        # the head pointer forwards one node
        value = self.head.value
        self.head = self.head.next 
        self.size -= 1

        # If the list is empty set the tail to null
        if self.isEmpty():
            self.tail = None
        # Do a memory cleanup of the previous node
        else:
            self.head.prev = None
        
        # Return the data that was at the first node we just removed
        print(f'removed {value}')
        return 

    # Remove the last value at the tail of the linked list, O(1)
    def removeLast(self):
        # Can't remove data from an empty list
        if self.isEmpty():
            print(RuntimeError("Empty List"))
            return
        
        # Extract the data at the tail and move
        # the tail pointer backwards one node
        value = self.tail.value
        self.tail = self.tail.prev
        self.size -= 1

        # If the list is now empty set the head to null
        if self.isEmpty():
            self.head = None
        # Do a memory clean of the node that was just removed
        else:
            self.tail.next = None
        
        # Return the data that was in the last node we just removed
        return

    # Remove an arbitrary node from the linked list, O(1)
    def __remove(self, node):
        # print(node.prev.value)
        # print(node.next.value)
        # If the node to remove is somewhere either at the
        # head or the tail handle those independently
        if node.prev == None:
            self.removeFirst()
            return
        if node.next == None:
            self.removeLast()
            return 
        
        # 1<=>2<=>3 to 1<=>3
        # Make the pointers of adjacent nodes skip over 'node'
        node.next.prev = node.prev
        node.prev.next = node.next
        # Temporarily store the data we want to return
        value = node.value

        # Memory cleanup
        node.value = None
        node.prev = node.next = None
        node = None
        self.size -= 1

        # Return the data in the node we just removed
        print(f'removed {value}')
        return 

    # Remove a node at a particular index, O(n)
    def removeAt(self,k=0):
        # Make sure the index provided is valid
        if (k < 0 or k >= self.size):
            print(IndexError(f'Index {k} is out of bounds!'))
            return 
        
        # Search from the front of the list
        if (k < self.size // 2):
            current = self.head
            curr_idx = 0
            while curr_idx != k:
                current = current.next
                curr_idx += 1
        else:
            current = self.tail
            curr_idx = self.size
            while curr_idx != k:
                current = current.prev
                curr_idx -= 1
        
        self.__remove(current)
        return

    # Remove a particular value in the linked list, O(n)
    def remove(self, new_node):
        current = self.head
        
        # Support searching for null
        if new_node == None:
            while current != None:
                if current.data is None:
                    self.__remove(current)
                    return print(f'Removed {current.value}')
                current = current.next
        # Search for non null object    
        else:
            while current != None:
                if new_node.value == current.value and new_node.prev == current.prev and new_node.next == current.next:
                    self.__remove(current)
                    return print(f'Removed {current.value}')
                current = current.next
        
        return print(f'Nothing to remove')

    """
    Print
    """
    def printHEAD(self):
        if not self.head:
            return print(ValueError("No element in HEAD"))
        
        print(f'HEAD: {self.head.value} | index: 0')

    def printTAIL(self):
        if not self.head:
            return print(ValueError("No element in TAIL"))
        
        print(f'TAIL: {self.tail.value} | index: {self.size-1}')

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

node.clear()

node.addFirst(e1)
node.add(e4)
# node.print()
node.removeFirst()
node.add(e2)
node.addFirst(e5)
# node.removeAt(1)
node.remove(e1)
node.add(e3)
# print(node.len())
# node.removeAt(2)
# print(e3.prev.value)
node.indexOf(e3)
node.print()
