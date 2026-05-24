from collections import deque


def sequence_reconstruction(original: list[int], seqs: list[list[int]]) -> bool:
    def build_graph() -> dict[int, set[int]]:
        graph = {val: set({}) for val in original}
        for seq in seqs:
            for dx in range(len(seq) - 1):
                graph[seq[dx]].add(seq[dx + 1])
        return graph

    def find_indegree(graph):
        indegree = {node: 0 for node in graph}  # dict
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

    q = deque()
    graph = build_graph()
    indegree = find_indegree(graph)

    for node in indegree:
        if indegree[node] == 0:
            q.append(node)

    if len(q) > 1:
        return False

    while len(q) > 0:
        node = q.popleft()
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
        if len(q) > 1:
            return False

    return True


original = [4, 1, 5, 2, 6, 3]
seqs = [[5, 2, 6, 3], [4, 1, 5, 2]]
assert sequence_reconstruction(original, seqs)
print("✅")
