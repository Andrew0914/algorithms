def letter_combinations_of_phone_number(digits: str) -> list[str]:
    res = []

    phone = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def get_edges(start_index: int):
        return phone[digits[start_index]]

    def is_leaf(start_index: int):
        return start_index == len(digits)

    def dfs(start_index: int, path: list[str]):
        if is_leaf(start_index):
            res.append("".join(path))  # add a copy of the path to the result
            return

        for edge in get_edges(start_index):
            path.append(edge)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res


print(letter_combinations_of_phone_number("56"))
