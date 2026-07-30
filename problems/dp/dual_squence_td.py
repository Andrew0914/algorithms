from functools import lru_cache


def distinct_subsequences(s: str, t: str) -> int:
    from functools import lru_cache

    @lru_cache(None)
    def count(i: int, j: int) -> int:
        # Matched all of t
        if j == len(t):
            return 1
        # Ran out of s before matching t
        if i == len(s):
            return 0

        # Skip s[i]
        result = count(i + 1, j)

        # Use s[i] if it matches t[j]
        print(f"s[{i}] == t[{j}] -> {s[i] == t[j]}")
        if s[i] == t[j]:
            result += count(i + 1, j + 1)

        return result

    return count(0, 0)


s = "babgbag"
t = "bag"
print(distinct_subsequences(s, t))
