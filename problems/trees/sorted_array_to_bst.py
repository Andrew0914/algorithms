from typing import Optional

from utils.tree_node import TreeNode

# Having a sorted array in ascending order use their values to create a height balanced tree.


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
