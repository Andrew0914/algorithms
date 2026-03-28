from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def checkSymmetri(
        self, left: Optional[TreeNode], right: Optional[TreeNode]
    ) -> bool:
        if [left, right] == [None, None]:
            return True

        if left is None or right is None:
            return False

        is_symmetric = left.val == right.val

        return (
            is_symmetric
            and self.checkSymmetri(left.left, right.right)
            and self.checkSymmetri(left.right, right.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.checkSymmetri(root.left, root.right)
