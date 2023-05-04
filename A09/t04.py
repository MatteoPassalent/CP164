"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-04-02"
-------------------------------------------------------
"""

from BST_linked import BST

bst = BST()


bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(20)


zero, one, two = bst.node_counts()

print(zero)
print(one)
print(two)
print()

print(20 in bst)
print()

value = bst.parent(20)
print(value)

value = bst.parent_r(20)
print(value)
