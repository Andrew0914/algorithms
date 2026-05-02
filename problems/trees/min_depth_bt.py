from typing import Optional

from utils.build_tree import build_tree
from utils.tree_node import TreeNode


class Solution:
    def getMinDepth(self, node: Optional[TreeNode], depth=0, min_depth=float("inf")):
        if not node:
            return min_depth

        if node and not node.left and not node.right:
            return min(depth + 1, min_depth)

        min_depth = self.getMinDepth(node.left, depth + 1, min_depth)
        min_depth = self.getMinDepth(node.right, depth + 1, min_depth)

        return min_depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return int(self.getMinDepth(root))


tree1 = build_tree([2, None, 3, None, 4, None, 5, None, 6])
# tree2 = build_tree([3, 9, 20, None, None, 15, 7])


sol = Solution()
print(sol.minDepth(tree1))
