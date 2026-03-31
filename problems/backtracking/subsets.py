def get_subsets_upto(number: int) -> list[int]:
    result: list[int] = []

    def is_leaf(start_index) -> bool:
        return start_index > number

    def backtrack(start_index, path=[]):
        result.append(path[:])
        if is_leaf(start_index):
            return

        for val in range(start_index, number + 1):
            path.append(val)
            backtrack(val + 1, path)
            path.pop()

    backtrack(1, [])
    return result


print(get_subsets_upto(2))
