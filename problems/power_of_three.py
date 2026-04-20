class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        reminder = n
        if -3 < reminder < 3:
            return False
        while reminder != -1 and reminder != 1:
            if -3 < reminder < 3:
                return False
            reminder = reminder / 3

        return True


sol = Solution()
sol.isPowerOfThree(-1)
