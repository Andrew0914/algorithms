# dynamic programming with grids
def unique_paths(m: int, n: int) -> int:
    row = [0] * n
    grid = [row] * m

    # filling base cases
    for r in range(m):
        grid[r][0] = 1

    for c in range(n):
        grid[0][c] = 1

    # calculate number of paths
    for r in range(1, m):
        for c in range(1, n):
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

    return grid[-1][-1]
