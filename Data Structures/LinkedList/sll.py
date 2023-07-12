# Initialized a Node struct that has two properties: its value and the pointer next
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Methods Included
    1. Append
    2. Pop
    3. Insert
    4. Delete
    5. Print 
    6. len
    7. Clear
"""

# SLL data structure
class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    """
    A traversal pointer (current) travel on the linked list and if no node is available in the next, it will assign the new node

    Travelling is O(n) since it starts with the head, which is the first one, and tail gets longer with a new value.

    Solution for optimization:
        Add a tail on the constructor -> O(1)

        Pop can't be implemented because the last element don't have access on its previous element in SLL but append can be O(1)

        But since a pointer (TAIL) is addressed at the end of the SLL, implementation is now O(1) when accessing the last element of SLL.
    
    The solution for inserting in head and tail is now O(1)
    """

    def insertAtTail(self, new_node):
        # current acts as the traversal pointer 
        current = self.tail

        # If the head has any NODE at all (truthy value)
        if current:
            current.next = new_node
            self.tail = current.next

            # while current.next:
            #     current = current.next
        else:
            self.head = new_node
            self.tail = new_node
        
        self.size += 1
    
    def insertAtHead(self,new_node=None):
        current = new_node
        
        if current:
            current.next = self.head
            self.head = current
        
        self.size += 1
    
    def len(self):
        print(f'{self.size}')

    """
    Printing HEAD and TAIL of SLL -> O(1)

    Printing the entire SLL -> O(n)
    """
    def printHEAD(self):
        print(f'HEAD: {self.head.value}')

    def printTAIL(self):
        print(f'TAIL: {self.tail.value}')

    def print(self):
        current = self.head

        while current:
            print(f'{current.value}',end="->")
            current = current.next
        print("None")

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

node = SingleLinkedList()

node.insertAtTail(e1)

node.insertAtTail(e2)
node.insertAtHead(e3)
node.insertAtHead(e4)
node.insertAtTail(e5)

node.printHEAD()
node.printTAIL()

node.len()

node.print()

    
    