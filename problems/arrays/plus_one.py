class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        len_digits = len(digits)
        for idx in reversed(range(len_digits)):
            current = digits[idx]
            curr_sum = current + carry
            if curr_sum % 10 != 0 or curr_sum == 0:
                carry = 0
                digits[idx] = curr_sum
            else:
                carry = 1
                digits[idx] = 0

        if carry > 0:
            digits.insert(0, carry)

        return digits


print(Solution().plusOne([1, 0, 0]))
