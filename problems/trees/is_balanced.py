from utils.tree_node import TreeNode


def check_balance(node: "TreeNode | None"):
    if not node:
        return (True, -1)

    is_left_balanced, left_height = check_balance(node.left)
    is_right_balanced, right_height = check_balance(node.right)

    subtrees_balanced = is_left_balanced and is_right_balanced
    current_balance = abs(left_height - right_height) <= 1

    new_balance = subtrees_balanced and current_balance

    return (new_balance, max(left_height + 1, right_height + 1))


def is_balanced(node: "TreeNode | None"):
    balanced, _ = check_balance(node)

    return is_balanced
