from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # is a leaf
        if root and not root.left and not root.right:
            return targetSum == root.val

        if self.hasPathSum(root.left, targetSum - root.val):
            return True

        if self.hasPathSum(root.right, targetSum - root.val):
            return True

        return False


root = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
seven = TreeNode(7)

root.left = four
root.right = five
four.right = seven
targetSum = 8

s = Solution()
assert s.hasPathSum(root, targetSum)
