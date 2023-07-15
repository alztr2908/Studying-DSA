"""
Resources:
    - https://github.com/hariuserx/MinHeap/blob/master/src/MinHeapWithoutArrays.java#L77
    - https://github.com/williamfiset/DEPRECATED-data-structures/blob/master/com/williamfiset/datastructures/priorityqueue/BinaryHeap.java
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.prevTail = None

class MinHeapTree:
    def __init__(self,root=None):
        self.root = root
        self.tail = None
        self.size = 0
    
    """
    Helper
    """
    # Checks if the tree is empty 
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __isEmpty(self):
        if self.size == 0:
            return True
        
        return False
    
    # def isEmpty(self):
    #     pass

    def peek(self):
        return print(f'Root of tree: {self.root.value}')
    
    def setTail(self, node):
        # Root - node that has no parent
        # If we reach this stage that means a level is completely filled
        # and we need to proceed to the next level by going to the extreme left.
        if node.parent is None:
            self.tail = node
            
        # Traverse until it reached the most left at the bottom
            while self.tail.left is not None:
                self.tail = self.tail.left

        # If tail is in the left, assign to right 
        elif node.parent.left == node:
            self.tail = node.parent.right
            
        # Traverse until it reached the most left at the bottom
            while self.tail.left is not None:
                self.tail = self.tail.left
        
        # If tail is in the right, go back to its parent node 
        elif node.parent.right == node:
            self.setTail(node.parent)
    
    def swap(self,a,b):
        a.value, b.value = b.value, a.value
           
    """
    Add

    Tail is in the parent nodes of the tree
    PrevTail is pointer to the last parent node before tail
    
    If the tail has two children, tail will be the right child of prevTail
    
    If the right child of prevTail has two children, tail will be the left child, prevTail will be the tail then tail will be the left child of prevTail

             1  prevTail
            / \ 
      tail 2   3 
          /  
         4

                  1  
                 / \ 
                2   3 prevTail
               / \ / \  
         tail 4  5 6  7
             /
            8 ..........
    """
    # Inserting a new node to the heap -> O(log(n))
    def insert(self,new_node):
        if self.root is None:
            self.root = self.tail = new_node
            self.size += 1
            return
        
        if self.tail.left is None:
            self.tail.left = new_node
            self.tail.left.parent = self.tail
            # Retaining heap property
            self.swim(self.tail.left)
        else:
            self.tail.right = new_node
            self.tail.right.parent = self.tail
            # Retaining heap property
            self.swim(self.tail.right)

            # Since parent has two children assign different tail
            currentTail = self.tail
            self.setTail(self.tail)
            self.tail.prevTail = currentTail
        
        self.size += 1

    def swim(self,node):
        if node.parent is None:
            return
        
        if node.parent.value > node.value:
            self.swap(node.parent, node)
            self.swim(node.parent)  
            
    """
    Delete
    """

    """
    Traverse
    """

    """
    Print - implemented using BFS
    """
    def print(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0) # dequeue 
            print(current.value,end="->")
            
            # enqueue left and right children
            if current.left is not None:
                queue.append(current.left)
                
            if current.right is not None:
                queue.append(current.right)
        print()




e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
e7 = Node(7)
e8 = Node(8)

heap = MinHeapTree()
heap.insert(e4)
heap.peek()
heap.insert(e2)
heap.peek()
heap.insert(e1)
heap.peek()
heap.insert(e5)
# heap.peek()

heap.print()
# print(heap.preorder_recursive())