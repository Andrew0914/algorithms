from dsa.tree.b_tree_node import BinaryTreeNode
from dsa.tree.binary_search_tree import BinarySearchTree

# Leaf nodes
node1 = BinaryTreeNode(value=1)
node3 = BinaryTreeNode(value=3)  # Pred.
node5 = BinaryTreeNode(value=5)
node8 = BinaryTreeNode(value=8)

# Internal nodes (bottom-up)
node2 = BinaryTreeNode(value=2, left=node1, right=node3)
node9 = BinaryTreeNode(value=9, left=node8)

node4 = BinaryTreeNode(value=4, left=node2, right=node5)  # N
node7 = BinaryTreeNode(value=8, right=node9)

node6 = BinaryTreeNode(value=6, left=node4, right=node7)  # Root

# Wire up parent pointers
node1._parent = node2
node3._parent = node2
node8._parent = node9

node2._parent = node4
node5._parent = node4
node9._parent = node7

node4._parent = node6
node7._parent = node6


bst = BinarySearchTree(root=node6)
