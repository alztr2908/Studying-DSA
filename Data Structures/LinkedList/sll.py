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
    

    def append(self, new_node):
        """
        Appending the singly linked list -> O(n) 

        A traversal pointer (current) travel on the linked list and if no node is available in the next, it will assign the new node

        Travelling is O(n) since it starts with the head, which is the first one, and tail gets longer with a new value.

        Solution for optimization:
            Add a tail on the constructor -> O(1)
        """
        
        # current acts as the traversal pointer 
        current = self.head

        # If the head has any NODE at all (truthy value)
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def print(self):
        current = self.head

        while current:
            print(f'{current.value}',end="->")
            current = current.next
        print("None")

e1 = Node(1)
e2 = Node(2)

node = SingleLinkedList()

node.append(e1)

node.append(e2)

node.print()

    
    