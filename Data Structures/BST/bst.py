"""
    - Find
    - Remove
    - Insert
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.head = None
        # self.curr = None
        self.sz = 0

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.sz == 0

    def _insert(self, node, new_node):
        if self.isEmpty():
            self.head = node
            self.sz += 1
            return

        current = node

        if current.left is None and current.val < new_node.val:
            current.left = new_node
            self.sz += 1
            return
        elif current.right is None and current.val > new_node.val:
            current.right = new_node
            self.sz += 1
            return

        # Recurse down left subtree
        if current.val <= new_node.val:
            self.insert(current.left)
        # Recurse down right subtree
        elif current.val > new_node.val:
            self.insert(current.right)

        return

    def bfs(self):
        queue = [self.head]
        if queue[0] is None:
            queue.pop()
        while queue:
            current = queue.pop(0)  # dequeue
            print(current.val, end="->")

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

bst = BSTree()
bst.insert(e1)
bst.insert(e2)
bst.insert(e3)
bst.insert(e4)
bst.insert(e5)
bst.bfs()
