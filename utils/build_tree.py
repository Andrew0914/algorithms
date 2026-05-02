from collections import deque
from utils.tree_node import TreeNode


def build_tree(data: list) -> "TreeNode | None":
    """Build a binary tree from a level-order list (LeetCode format).

    Example: [2, None, 3, None, 4, None, 5, None, 6]
    """
    if not data:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        node = queue.popleft()

        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1

        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    tree = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    print(tree)
