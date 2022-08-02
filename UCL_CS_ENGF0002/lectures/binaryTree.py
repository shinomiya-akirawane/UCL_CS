class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = treeNode(key, value)
        else:
            self.root.insert(key, value)

    def find(self, key):
        if self.root is None:
            return None
        else:
            node = self.root.find(key)
            if node is None:
                return None
            else:
                return node.value

    def delete(self, key):
        if self.root is None:
            return
        else:
            if(self.root.find(key) is None):
                return
            else:
                self.root = self.root.delete(key)
    def walk(self):
        if self.root is None:
            return
        yield from self.root.walk()



class treeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                n = treeNode(key, value)
                self.left = n
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                n = treeNode(key, value)
                self.right = n
            else:
                self.right.insert(key, value)

    def find(self, key):
        if self.key == key:
            return self
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(key)

    def maxkey(self):
        if self.right is None:
            return self.key
        return self.right.maxkey()

    def delete(self, key):
        if self.key == key:
            # delete this node
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                maxkey = self.left.maxkey()
                maxnode = self.left.find(maxkey)
                self.left.delete(maxkey)
                maxnode.left = self.left
                maxnode.right = self.right
                return maxnode
        elif key < self.key:
            # ask left children to delete
            self.left = self.left.delete(key)
        else:
            # ask right children to delete
            self.right = self.right.delete(key)
        return self
    def walk(self):
        if self.left is not None:
            yield from self.left.walk()
        yield (self.key,self.value)
        if self.right is not None:
            yield from self.right.walk()


def testAddFind():
    tree = treeNode(10, 'ten')
    tree.insert(20, 'twenty')
    tree.insert(5, 'five')
    node = tree.find(5)
    print(node.key)
    print(node.value)

    tree.delete(5)
    node = tree.find(5)
    print(node)


testAddFind()
