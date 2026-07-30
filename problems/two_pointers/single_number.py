import functools
from operator import xor


class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        if len(nums) <= 1:
            return nums[0]

        return functools.reduce(xor, nums, 0)


s = Solution()
print(s.singleNumber([2, 2, 1]))
