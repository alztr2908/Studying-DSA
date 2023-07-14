class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class sllQueue:
    def __init__(self,head=None):
        self.head = head
        self.tail = None
        self.size = 0
    
    """
    Helper Methods
    """
    def __isEmpty(self):
        if self.size == 0:
            return True
        
        return False
    
    def isEmpty(self):
        if self.__isEmpty():
            return print("Empty queue")
        
        return print("NOT Empty queue: {self.size}")
    
    def peek(self):
        return print(f'Current HEAD: {self.head.value}')
    
    def contains(self):
        pass
    
    def indexOf(self):
        pass

    """
    Enqueue
    """
    def enqueue(self,new_node):
        if self.__isEmpty():
            self.head = self.tail = new_node
            self.size += 1
            return 
        
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1


    """
    Dequeue
    """
    def dequeue(self):
        pass
    
    def removal(self):
        pass

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

node = sllQueue()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

node.enqueue(e1)
node.enqueue(e2)
node.enqueue(e3)
node.enqueue(e4)

node.isEmpty()
node.print()
