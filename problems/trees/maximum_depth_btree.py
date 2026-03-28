from typing import Optional

from utils.tree_node import TreeNode


# Find the number of the longest path from root to the farest leaf.
class Solution:
    def getMaxDepth(self, node: Optional[TreeNode], depth=0) -> int:
        if not node:
            return depth

        depth = depth + 1

        depth_x = self.getMaxDepth(node.left, depth)
        depth_y = self.getMaxDepth(node.right, depth)

        return max(depth_x, depth_y)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        initial_depth = 0

        return self.getMaxDepth(root, initial_depth)


"""
Tree structure (depth 5):
            1
           / \
          2   3
         /
        4
       /
      5
     /
    6
"""
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, TreeNode(5, TreeNode(6)))),
    TreeNode(3),
)

s = Solution()
print(s.maxDepth(root))  # Expected: 5
