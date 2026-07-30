def print_matrix(matrix):
    for row in matrix:
        print(row)


def min_distance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # base cases
    ## insertions
    for j in range(n + 1):
        dp[0][j] = j
    ## deletions
    for i in range(m + 1):
        dp[i][0] = i

    # inner cases
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # free
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # with min cost: replace, delete, insert
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


word1 = "horse"
word2 = "ros"

assert min_distance(word1, word2) == 3
