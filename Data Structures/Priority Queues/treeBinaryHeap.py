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
    def _isEmpty(self):
        if self.size == 0:
            return True
        
        return False
    
    # def isEmpty(self):
    #     pass

    def peek(self):
        if self.root is None:
            return print(RuntimeError("Heap is empty"))

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
    
    def nodeSwap(self,a,b):
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
        # print(f'root before: {self.root.value}')
        # print(f'tail before: {self.tail.value}')

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
        
        # print(f'root after: {self.root.value}')
        # print(f'tail after: {self.tail.value}')
        # if self.tail.prevTail:
        #     print(f'prevTail after: {self.tail.prevTail.value}')
        
        self.size += 1

    # Traversing new node to retain heap invariant -> O(log(n))
    def swim(self,node):
        if node.parent is None:
            return
        
        if node.parent.value > node.value:
            self.nodeSwap(node.parent, node)
            self.swim(node.parent)  
            
    """
    Delete

    Poll 
        - swap self.tail child with root
        - set self.tail.child be null
        - if both self.tail.child is null, move self.tail to prevtail 
        - move prevtail to prevtail.prevtail
    """
    def poll(self):
        if self._isEmpty():
            return print(RuntimeError("Heap is empty"))

        # print(f'hi: {self.tail.value}')
        # print(f'hello: {self.root.value}')

        # If node_length < 3 
        # self.tail == self.root only will cause an error
        # check if root still has children
        if self.tail == self.root and self.tail.left is None:
            self.tail = None
            self.root = None
            self.size -= 1
            return 
        
        if self.tail.right is not None:
            self.nodeSwap(self.tail.right, self.root)
            self.tail.right = None
            self.sink(self.root)
        
        elif self.tail.left is not None:
            self.nodeSwap(self.tail.left, self.root)
            self.tail.left = None
            self.sink(self.root)
        
        else:
            self.tail = self.tail.prevTail
            self.poll()
            self.size += 1
        
        self.size -= 1
    
    def sink(self,node):
        if node is None or node.left is None:
            return

        min_val = node.left

        if node.right is not None and min_val.value > node.right.value:
            min_val = node.right
        
        if min_val.value < node.value:
            self.nodeSwap(min_val,node)
            self.sink(min_val)
            
    """
    Traverse
    """

    """
    Print - implemented using BFS
    """
    def print(self):
        queue = [self.root]
        if queue[0] is None:
            queue.pop()
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
heap.insert(e2)
heap.insert(e5)
heap.insert(e6)
heap.insert(e7)
heap.insert(e8)
heap.peek()
heap.poll()
heap.peek()
heap.poll()
heap.insert(e1)
# heap.peek()

heap.print()
# print(heap.preorder_recursive())