"""
Converted to python code from 
link: https://github.com/williamfiset/DEPRECATED-data-structures/blob/master/com/williamfiset/datastructures/unionfind/UnionFind.java
"""


class UnionFind:
    def __self__(self):
        # The number of elements in this union find
        self.size = 0
        # Used to track the size of each of the component
        self.sz = []
        # id[i] points to the parent of i, if id[i] = i then i is a root node
        self.id = []
        # Tracks the number of components in the union find
        self.numComponents = 0

    def UnionFind(self, size):
        if size <= 0:
            return print(ValueError())

        self.size = self.numComponents = size

        self.sz = [0]*size
        self.id = [0]*size

        for i in range(size):
            self.id[i] = i  # link to itself (self root)
            self.sz[i] = 1  # each component is originally of size one

    # Find which component/set 'p' belongs to, takes amortized constant time.
    def find(self, p):
        # Find root of component/set
        root = p
        while (root != self.id[root]):
            root = self.id[root]

        # Compress the path leading back to the root.
        # Doing this operation is called "path compression"
        # and is what gives us amortized time complexity.
        while (p != root):
            next = self.id[p]
            self.id[p] = root
            p = next

        print(f"Root of {p}: {root}")
        return root

    # This is an alternative recursive formulation for the find method
    # def find(self, p) {
    #   if (p == id[p]):
    #        return p
    #   return id[p] = find(id[p])
    # }

    # Return whether or not the elements 'p' and
    # 'q' are in the same components/set.
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Return the size of the components/set 'p' belongs to
    def componentSize(self, p):
        return self.sz[self.find(p)]

    # Return the number of elements in this UnionFind/Disjoint set
    def sizeUnionFind(self):
        return self.size

    # Returns the number of remaining components/sets
    def components(self):
        return self.numComponents

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        # These elements are already in the same group!
        if root1 == root2:
            return print("Already on the same group")

        # Merge smaller component/set into the larger one.
        if (self.sz[root1] < self.sz[root2]):
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        self.numComponents -= 1


node = UnionFind()
node.UnionFind(10)
print(node.sizeUnionFind())
node.find(2)
node.unify(0, 1)
node.unify(0, 1)
print(node.connected(0, 1))
