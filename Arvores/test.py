from random import sample, seed
from Tree import BinarySeachTree


values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]

tree = BinarySeachTree()

for v in values:
    tree.insert(v)

tree.inorder_traversal()
print("\n------")
tree.levelorder_traversal()
print("\n------")
print("Máximo:", tree.max())
print("Mínimo:", tree.min())