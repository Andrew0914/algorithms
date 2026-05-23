from collections import deque


def task_scheduling(tasks: list[str], requirements: list[list[str]]) -> list[str]:
    def find_indegree():
        indegree = {node: 0 for node in tasks}  # dict
        for requirement in requirements:
            dependant_task = requirement[1]
            indegree[dependant_task] += 1
        return indegree

    res = []
    q = deque()
    indegree = find_indegree()
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for req in requirements:
            if req[0] != node:
                continue
            indegree[req[1]] -= 1
            if indegree[req[1]] == 0:
                q.append(req[1])

    return res if len(tasks) == len(res) else []


tasks = ["a", "b", "c", "d"]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

assert task_scheduling(tasks, requirements) == ["a", "c", "b", "d"]
print("✅")
