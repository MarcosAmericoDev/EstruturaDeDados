class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        if data:
            node = TreeNode(data) #Criação de um nó a partir de um dado
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node.data, end=' ')
        if node.right:
            self.inorder_traversal(node.right)
    
    def postorder_traversel(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversel(node.left)
        if node.right:
            self.postorder_traversel(node.right)
        print(node.data)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

class BinarySeachTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if self.root is None:
            self.root = TreeNode(value)
        elif value < parent.data:
            parent.left = TreeNode(value)
        else: 
            parent.right = TreeNode(value)

    def search(self, value):
        return self._search(value, self.root)
    
    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySeachTree(node.data)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    n1 = TreeNode('I')
    n2 = TreeNode('N')
    n3 = TreeNode('S')
    n4 = TreeNode('C')
    n5 = TreeNode('R')
    n6 = TreeNode('E')
    n7 = TreeNode('V')
    n8 = TreeNode('A')
    n9 = TreeNode('5')
    n10 = TreeNode('3')

    n10.left = n6
    n10.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.left = n3
    n9.left = n8
    n8.right = n7

    tree.root = n10
    tree.postorder_traversel()
    print("Altura:", tree.height(n5))