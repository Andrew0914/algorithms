from utils.build_n_ary_tree import build_n_ary_tree
from utils.n_ary_node import NAryNode


class Solution:
    def maxDepth(self, root: "NAryNode | None") -> int:
        if not root:
            return 0

        depth = 1

        for child in root.children:
            depth = max(depth, self.maxDepth(child) + 1)

        return depth


tree = build_n_ary_tree([1, None, 3, 2, 4, None, 5, 6])


sol = Solution()
print(sol.maxDepth(tree))
