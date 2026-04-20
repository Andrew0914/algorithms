from utils.tree_node import TreeNode


def calculate_heigh(node: "TreeNode | None"):
    if not node:
        return -1

    left = 1 + calculate_heigh(node.left)
    right = 1 + calculate_heigh(node.right)

    return max(left, right)


if __name__ == "__main__":
    root = TreeNode(1)
    node2 = TreeNode(2)
    root.left = node2
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)

    print(calculate_heigh(node2))
