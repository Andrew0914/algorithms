from collections import deque


def num_steps(init_pos: list[list[int]]) -> int:
    visited = set([])

    def swap(board: str, empty_index: int, idx: int):
        min_pos = min(empty_index, idx)
        max_pos = max(empty_index, idx)
        return (
            board[:min_pos]
            + board[max_pos]
            + board[min_pos + 1 : max_pos]
            + board[min_pos]
            + board[max_pos + 1 :]
        )

    def get_neighbors(board: str):
        empty_index = board.index("0")
        row_limits = [-3, 3]
        col_limits = [-1, 1]
        max_board = len(board)
        delta = 3
        neighbors = []
        # swap valid column values
        for limit in col_limits:
            idx = empty_index + limit
            if 0 <= idx < max_board and idx // delta == empty_index // delta:
                neighbors.append(swap(board, empty_index, idx))
        # swap valid row values
        for limit in row_limits:
            idx = empty_index + limit
            if 0 <= idx < max_board:
                neighbors.append(swap(board, empty_index, idx))
        return neighbors

    board = "".join([str(item) for sublist in init_pos for item in sublist])
    target = "123450"

    if board == target:
        return 0

    queue = deque([board])
    visited.add(board)
    distance = 0
    while queue:
        n = len(queue)
        distance += 1
        for _ in range(n):
            curr_board = queue.popleft()
            for neighbor_board in get_neighbors(curr_board):
                if neighbor_board == target:
                    return distance
                if neighbor_board not in visited:
                    queue.append(neighbor_board)
                    visited.add(neighbor_board)
    return -1


init_pos = [[4, 1, 3], [2, 0, 5]]
assert num_steps(init_pos) == 1
