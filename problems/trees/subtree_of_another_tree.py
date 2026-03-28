from utils.tree_node import TreeNode as Node


def is_same_tree(node1, node2):
    return True


def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:

    return (
        root.val == sub_root.val
        and is_same_tree(root.left, sub_root.left)
        and is_same_tree(root.right, sub_root.right)
    )


root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3

sub_root = Node(2)

subtree_of_another_tree(root, sub_root)
