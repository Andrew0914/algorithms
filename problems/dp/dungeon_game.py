def dungeon_game(dungeon: list[list[int]]) -> int:
    if not dungeon:
        return 0

    m = len(dungeon)
    n = len(dungeon[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]
    # princess
    dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
    # calculate last row
    for c in reversed(range(n - 1)):
        dp[-1][c] = max(1, dp[-1][c + 1] - dungeon[-1][c])

    # calculate last col
    for r in reversed(range(m - 1)):
        dp[r][-1] = max(1, dp[r + 1][-1] - dungeon[r][-1])

    # calculate inner cells
    for r in reversed(range(m - 1)):
        for c in reversed(range(n - 1)):
            dp[r][c] = max(1, min(dp[r][c + 1], dp[r + 1][c]) - dungeon[r][c])

    return dp[0][0]


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
assert dungeon_game(dungeon) == 7
