from collections import deque

INF = 2147483647


def map_gate_distances(dungeon_map: list[list[int]]) -> list[list[int]]:
    max_row = len(dungeon_map)
    max_col = len(dungeon_map[0])

    def get_tiles(x: int, y: int) -> list[tuple[int, int]]:
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        tiles = []
        for dx in range(len(delta_row)):
            tile_x = x + delta_row[dx]
            tile_y = y + delta_col[dx]
            if 0 <= tile_x < max_row and 0 <= tile_y < max_col:
                tiles.append((tile_x, tile_y))
        return tiles

    queue = deque([])
    # Initialize queue from gates
    for rx in range(max_row):
        for cy in range(max_col):
            if dungeon_map[rx][cy] == 0:
                queue.append((rx, cy))

    # BFS to calculate distances
    while len(queue) > 0:
        x, y = queue.popleft()
        for tx, ty in get_tiles(x, y):
            if dungeon_map[tx][ty] == INF:
                dungeon_map[tx][ty] = dungeon_map[x][y] + 1
                queue.append((tx, ty))
    return dungeon_map


map = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]

result = map_gate_distances(map)
print(result)
