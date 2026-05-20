from collections import deque


def count_number_of_islands(grid: list[list[int]]) -> int:
    max_rows = len(grid)
    max_cols = len(grid[0])

    def get_neighbours(node: tuple[int, int]) -> list[tuple[int, int]]:
        row_limits = [-1, 0, 1, 0]
        col_limits = [0, 1, 0, -1]
        cr, cc = node
        neighbours = []
        for rdx in range(len(row_limits)):
            new_r = cr + row_limits[rdx]
            new_c = cc + col_limits[rdx]
            if 0 <= new_r < max_rows and 0 <= new_c < max_cols:
                neighbours.append((new_r, new_c))
        return neighbours

    def bfs(root: tuple[int, int]):
        queue = deque([root])
        while len(queue) > 0:
            nr, nc = queue.popleft()
            for nbr, nbc in get_neighbours((nr, nc)):
                if grid[nbr][nbc] == 0:
                    continue
                queue.append((nbr, nbc))
                grid[nbr][nbc] = 0

    count = 0
    for rdx in range(max_rows):
        for cdx in range(max_cols):
            if grid[rdx][cdx] == 0:
                continue
            bfs((rdx, cdx))
            count += 1

    return count


grid = [[0, 0], [1, 1]]
res = count_number_of_islands(grid)
print(res)
