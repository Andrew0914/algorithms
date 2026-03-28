# O(n)
def two_sum_hm(nums: list[int], target: int) -> list[int]:
     values = {}
     index = 0
     for num in nums:
         result = target - num
         if result in values:
             return [values[result], index]
         values[num] = index
         index += 1
     return []

print(two_sum_hm([2,11,15, 3, 7], 9))

# O(n^2)
def two_sum_arr(numbers: list[int], target: int) -> list[int]:
    index1 = 0
    index2 = 0
    for num in numbers:
        for num2 in numbers:
            if num + num2 == target:
                return [index1, index2]
            index2 += 1
        index1 += 1
    return []

print(two_sum_arr([2,11,15, 3, 7], 9))
