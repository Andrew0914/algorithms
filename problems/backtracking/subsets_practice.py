def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def dfs(start_index=0, path=[]):
        result.append(path[:])
        # is a leaf
        if start_index == len(nums):
            return

        for dx in range(start_index, len(nums)):
            path.append(nums[dx])
            dfs(dx + 1, path)
            path.pop()

        return

    dfs(0, [])
    return result


print(subsets([1, 2, 3]))
