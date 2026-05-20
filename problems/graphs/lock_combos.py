from collections import deque


def num_steps(target_combo: str, trapped_combos: list[str]) -> int:
    if target_combo == "0000":
        return 0

    visited = set(["0000"])
    trapped_set = set(trapped_combos)

    def get_neighbors(combo: str):
        digits = [int(i) for i in combo]
        neighbors = []
        for i in range(len(digits)):
            curr = digits[i]
            up_combo = combo[:i] + str((curr + 1) % 10) + combo[i + 1 :]
            down_combo = combo[:i] + str((curr - 1) % 10) + combo[i + 1 :]
            if up_combo not in trapped_set and up_combo not in visited:
                neighbors.append(up_combo)
                visited.add(up_combo)
            if down_combo not in trapped_set and down_combo not in visited:
                neighbors.append(down_combo)
                visited.add(down_combo)

        return neighbors

    queue = deque(["0000"])
    steps = 0
    while len(queue) > 0:
        level_size = len(queue)
        steps += 1
        for _ in range(level_size):
            curr_combo = queue.popleft()
            for neigbor_combo in get_neighbors(curr_combo):
                if neigbor_combo == target_combo:
                    return steps
                queue.append(neigbor_combo)

    return -1


target_combo = "1111"
trapped_combos = ["01112111", "1011", "1211", "1101", "1121", "1110", "1112"]


# assert num_steps(target_combo, trapped_combos) == 6, "Expected 6 steps❌"
print(num_steps(target_combo, trapped_combos))
