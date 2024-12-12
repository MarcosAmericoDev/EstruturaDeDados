from random import sample, seed
from Tree import BinarySeachTree

seed(77)

values = sample(range(1, 1000), 42)

bst = BinarySeachTree()
for v in values:
    bst.insert(v)

bst.inorder_traversal()

items = [1, 3, 963, 510, 1000]

for item in items:
    r = bst.search(item)
    if r is None:
        print(item, "não encontrado")
    else:
        print(r.root.data, "encontrado")