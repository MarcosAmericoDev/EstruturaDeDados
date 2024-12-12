class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data) #Criação de um nó a partir de um dado
            self.root = node
        else:
            self.root = None
            
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='') # Parênteses específicos para o nosso exemplo.
            self.inorder_traversal(node.left)
        print(node.data, end='')
        if node.right:
            self.inorder_traversal(node.right)
            print(')', end='')
    
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


if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n10 = Node('3')

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