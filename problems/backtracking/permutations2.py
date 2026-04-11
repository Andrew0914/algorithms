def permutations(letters: str) -> list[str]:
    result = []

    def is_leaf(start_index=0):
        # Indeed it superpass the last index ot the letters
        return start_index == len(letters)

    def backtrack(start_index=0, path=[]):

        if is_leaf(start_index):
            result.append("".join(path))
            return

        for letter in letters:
            # prune for permutations and not prune for combinations
            if letter in path:
                continue

            path.append(letter)
            backtrack(start_index + 1, path)
            path.pop()

    backtrack(0, [])
    return result


print(permutations("ab"))
