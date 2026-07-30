from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def get_island_land(row: int, col: int) -> list[tuple[int, int]]:
            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            land = []
            for x, y in offsets:
                if 0 <= row + x < rows and 0 <= col + y < cols:
                    # JUST LAND NEIGHBOURS
                    if grid[row + x][col + y] == 0:
                        land.append((row + x, col + y))
            return land

        def bfs(land: tuple[int, int]):
            q = deque([land])
            visited.add(land)
            valid_island = True
            while q:
                curr_row, curr_col = q.popleft()
                for row, col in get_island_land(curr_row, curr_col):
                    if (row, col) in visited:
                        continue
                    q.append((row, col))
                    visited.add((row, col))
                    # if a neighbor in border not closed
                    if row <= 0 or row >= rows - 1 or col <= 0 or col >= cols - 1:
                        valid_island = False

            return valid_island

        result = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                # just not visited land
                if grid[row][col] == 0 and (row, col) not in visited:
                    result += 1 if bfs((row, col)) else 0

        return result


grid = [
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
]
s = Solution()
assert s.closedIsland(grid) == 5
