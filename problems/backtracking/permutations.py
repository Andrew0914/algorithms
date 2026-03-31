def permutations(nums: list[int]) -> list[int]:
    results = []

    def backtrack(path=[]):

        if len(path) == len(nums):
            results.append(path[:])
            return

        for dx_num in range(len(nums)):
            if nums[dx_num] in path:
                continue
            path.append(nums[dx_num])
            backtrack(path)
            path.pop()

        return

    backtrack([])
    return results


print(permutations([1, 2]))
