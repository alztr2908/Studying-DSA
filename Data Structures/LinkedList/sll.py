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
        current = self.head
        
        if current:
            new_node.next = current
            self.head = new_node
    
        else:
            self.head = new_node
            self.tail = new_node         
        
        self.size += 1
    
    def insert(self,new_node,k):
        # If k > size then it will assign to TAIL
        if k > self.size:
            print(IndexError('K is out of bounds!'))
            k = self.size

        # Insert at HEAD
        if k == 0:
            self.insertAtHead(new_node)
            return
        
        # Insert at TAIL
        elif k == self.size:
            self.insertAtTail(new_node)
            return 

        current = self.head
        curr_idx = 0

        # Insert at middle -> O(n)
        if current:
            # Traverse until (target_idx - 1)th node
            while current.next and curr_idx < k-1:
                current = current.next
                curr_idx += 1

            ###### 1->2->(3)->4 
            # [in order] 3 next address: 4
            new_node.next = current.next
            # 2 next address: 3
            current.next = new_node 
        
        self.size += 1

    """
    Deleting at HEAD -> O(1)
    Deleting at TAIL -> O(n) 
        Since no access at the past address on the TAIL, it will be hard to access the previous element of TAIL, hence traverse until the element before TAIL and deallocate TAIL and make the current pointer TAIL

    Deleting at the middle -> O(n)
        Two traversal pinters (current1 and current2) travel on the linked list and if it reach (n-1)th node, current1 will stay there and current2 will be on the (n+1)th node

    Python have a garbage collector so no worries on deallocating the new node
    """

    def deleteAtHead(self):
        current = self.head

        if current:
            self.head = current.next 
            current.next = None

            self.size -= 1
        else: 
            print(ValueError("No elements to delete"))


    def deleteAtTail(self):
        current = self.head

        if current:
            while current.next != self.tail and current.next != None:
                current = current.next
            
            current.next = None
            self.tail = current

            if self.size == 1:
                self.head = None
                self.tail = None

            self.size -= 1
        
        else: 
            print(ValueError("No elements to delete"))


    def len(self):
        print(f'{self.size}')

    """
    Printing HEAD and TAIL of SLL -> O(1)

    Printing the entire SLL -> O(n)
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
        current = self.head
        self.printHEAD()
        self.printTAIL()

        while current:
            print(f'{current.value}',end="->")
            current = current.next
        print("None")
        print()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

node = SingleLinkedList()

# node.insertAtTail(e1)

# node.insertAtTail(e2)
# node.insertAtHead(e3)
# node.insertAtHead(e4)
# node.insertAtTail(e5)


# e7 = Node(7)
# node.insert(e7,0)
# node.printHEAD()
# e6 = Node(6)
# node.insert(e6, 3)
# node.insert(e5,1)
# node.insert(e4,2)
# node.insertAtHead(e1)
# node.insert(e2,1)
# node.print()

node.insertAtTail(e1)
node.print()

# node.deleteAtTail()
node.deleteAtTail()
node.print()

# node


    