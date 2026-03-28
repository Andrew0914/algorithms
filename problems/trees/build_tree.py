from utils.tree_node import TreeNode


def build_tree_recursive(
    preorder: list[int],
    preorder_index: int,
    inorder_start: int,
    size: int,
    value_to_index: dict,
) -> TreeNode | None:
    if size <= 0:
        return None

    root_value = preorder[preorder_index]
    inorder_root_index = value_to_index[root_value]
    left_subtree_size = inorder_root_index - inorder_start

    left_child = build_tree_recursive(
        preorder, preorder_index + 1, inorder_start, left_subtree_size, value_to_index
    )
    right_child = build_tree_recursive(
        preorder,
        preorder_index + 1 + left_subtree_size,
        inorder_root_index + 1,
        size - 1 - left_subtree_size,
        value_to_index,
    )

    return TreeNode(root_value, left_child, right_child)


def construct_binary_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    value_to_index = {val: idx for idx, val in enumerate(inorder)}

    return build_tree_recursive(preorder, 0, 0, len(preorder), value_to_index)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

construct_binary_tree(preorder, inorder)
