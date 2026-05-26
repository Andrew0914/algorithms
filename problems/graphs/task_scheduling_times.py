from collections import deque


def task_scheduling_2(
    tasks: list[str], times: list[int], requirements: list[list[str]]
) -> int:
    def find_indegree():
        indegree = {node: 0 for node in tasks}  # dict
        for requirement in requirements:
            dependant_task = requirement[1]
            indegree[dependant_task] += 1
        return indegree

    q = deque()
    indegree = find_indegree()
    tasks_times = {task: times[dx] for dx, task in enumerate(tasks)}
    acc_times = {task: 0 for task in tasks}

    total = 0
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
            acc_times[node] = tasks_times[node]
            total = max(total, acc_times[node])

    while len(q) > 0:
        node = q.popleft()
        for req in requirements:
            if req[0] != node:
                continue
            indegree[req[1]] -= 1
            acc_times[req[1]] = max(
                acc_times[req[1]], acc_times[node] + tasks_times[req[1]]
            )
            total = max(total, acc_times[req[1]])
            if indegree[req[1]] == 0:
                q.append(req[1])

    return total


tasks = ["a", "b", "c", "d", "f", "g", "h"]
times = [1, 1, 1, 1, 1, 100, 1]
requirements = [["a", "b"], ["c", "b"], ["d", "b"], ["b", "f"], ["g", "f"]]

assert task_scheduling_2(tasks, times, requirements) == 101
print("✅")

# TODO:
# We need to know how to choise the critical path in order to count its tasks times only
# Which node finish erlier and has the next dependency that also finish erlier
