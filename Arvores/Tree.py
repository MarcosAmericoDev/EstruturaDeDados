from Queue import Queue

ROOT = "root"
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

    def inorder_traversal(self, node=ROOT):
        if node is ROOT:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node.data, end=' ')
        if node.right:
            self.inorder_traversal(node.right)
    
    def postorder_traversal(self, node=ROOT):
        if node is ROOT:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.data)
    
    def height(self, node=ROOT):
        if node is ROOT:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        return max(hleft, hright) + 1

    
    def levelorder_traversal(self, node=ROOT):
        if node is ROOT:
            node = self.root

        queue = Queue()
        queue.enQueue(node)
        while not queue.isEmpty():
            node = queue.deQueue()
            if node.left:
                queue.enQueue(node.left)
            if node.right:
                queue.enQueue(node.right)
            print(node.data, end=" ")
    
    def recursiveSearch(self, serchingValue, node=ROOT):
        if node is ROOT:
            node = self.root
        if node.data == serchingValue:
            print(serchingValue, "encontrado")
            return 
        if node.left:
            self.recursiveSearch(serchingValue, node.left)
        if node.right:
            self.recursiveSearch(serchingValue, node.right)
    
    def interactiveSearch(self, valueToSearch, node=ROOT):
        if node is ROOT:
            node = self.root
        queue = Queue()
        queue.enQueue(node)
        while not queue.isEmpty():
            node = queue.deQueue()
            if node.data == valueToSearch:
                print(valueToSearch, "encontrado!")
                return
            if node.left:
                queue.enQueue(node.left)
            if node.right:
                queue.enQueue(node.right)
        


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
    
    def search(self, value, node=ROOT):
        if node is ROOT:
            node = self.root
        if node is None:
            return node
        if node.data == value:
            return BinarySeachTree(node.data)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)
    
    def min(self, node=ROOT):
        if node is ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data
    
    def max(self, node=ROOT):
        if node is ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=ROOT):
        if node is ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            # if node.left is None and node.right is None:
            #     return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)

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
    tree.postorder_traversal()
    print("Altura:", tree.height(n5))