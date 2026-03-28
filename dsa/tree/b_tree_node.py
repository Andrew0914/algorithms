class BinaryTreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

    def value(self):
        return self._value

    def left(self) -> "BinaryTreeNode | None":
        return self._left

    def right(self) -> "BinaryTreeNode | None":
        return self._right

    def parent(self) -> "BinaryTreeNode | None":
        return self._parent

    def find_max_in_subtree(self):
        parent = None
        node: BinaryTreeNode = self
        while node.right() is not None:
            parent = node
            node = node.right()  # type: ignore[assignment]
        return node, parent

    def find_min_in_subtree(self):
        parent = None
        node: BinaryTreeNode = self
        while node.left() is not None:
            parent = node
            node = node.left()  # type: ignore[assignment]
        return node, parent
