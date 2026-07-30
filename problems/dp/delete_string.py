from string import ascii_lowercase


def delete_string(costs: list[int], s1: str, s2: str) -> int:

    m = len(s1)
    n = len(s2)
    char_dict = {char: i for i, char in enumerate(ascii_lowercase)}

    def cost(c):
        return costs[char_dict[c]]

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # base cases
    ## insertions
    for j in range(1, n + 1):
        dp[0][j] = cost(s2[j - 1]) + dp[0][j - 1]

    ## deletions
    for i in range(1, m + 1):
        dp[i][0] = cost(s1[i - 1]) + dp[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + cost(s1[i - 1]), dp[i][j - 1] + cost(s2[j - 1])
                )

    return dp[-1][-1]


costs = [
    1,
    2,
    3,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
s1 = "abb"
s2 = "bba"

assert delete_string(costs, s1, s2) == 2
