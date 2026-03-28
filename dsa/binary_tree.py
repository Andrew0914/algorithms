from utils.tree_node import TreeNode


class BinaryTree:
    def __init__(self, root: "TreeNode | None" = None):
        self.root = root

    def search(self, value: int, node: "TreeNode | None" = None) -> "TreeNode | None":
        if node is None or value == node.value:
            return node
        elif value < node.value:
            return self.search(value, node.leftChild)
        else:
            return self.search(value, node.rightChild)

    def insert(self, value: int, node: "TreeNode | None" = None):
        if node is None:
            return TreeNode(value)

        if value <= node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)
            else:
                self.insert(value, node.leftChild)
        else:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
            else:
                self.insert(value, node.rightChild)

    def delete(self, valueToDelete, node):
        # The base case is when we’ve hit the bottom of the tree,
        # and the parent node has no children:
        if node is None:
            return None
        # If the value we’re deleting is less or greater than the current node,
        # we set the left or right child respectively to be
        # the return value of a recursive call of this very method on the current
        # node’s left or right subtree.
        elif valueToDelete < node.value:
            node.leftChild = self.delete(valueToDelete, node.leftChild)
            # We return the current node (and its subtree if existent) to
            # be used as the new value of its parent’s left or right child:
            return node
        elif valueToDelete > node.value:
            node.rightChild = self.delete(valueToDelete, node.rightChild)
            return node
        # If the current node is the one we want to delete:
        elif valueToDelete == node.value:
            # If the current node has no left child, we delete it by
            # returning its right child (and its subtree if existent)
            # to be its parent’s new subtree:
            if node.leftChild is None:
                return node.rightChild
                # (If the current node has no left OR right child, this ends up
                # being None as per the first line of code in this function.)
            elif node.rightChild is None:
                return node.leftChild
                # If the current node has two children, we delete the current node
                # by calling the lift function (below), which changes the current node’s
            # value to the value of its successor node:
            else:
                node.rightChild = self.lift(node.rightChild, node)
                return node

    def lift(self, node, nodeToDelete):
        # If the current node of this function has a left child,
        # we recursively call this function to continue down
        # the left subtree to find the successor node.
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        # If the current node has no left child, that means the current node
        # of this function is the successor node, and we take its value
        # and make it the new value of the node that we’re deleting:
        else:
            nodeToDelete.value = node.value
            # We return the successor node’s right child to be now used
            # as its parent’s left child:
            return node.rightChild


# Crafting the tree
node2 = TreeNode(60)
node = TreeNode(40, None, None)
root = TreeNode(50, node, node2)
tree = BinaryTree(root)

# tree representation
#       50
#      /  \
#     40  60
#    / \
#   30 45


tree.insert(100, root)

print(root)
