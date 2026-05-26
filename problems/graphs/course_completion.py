from collections import deque


def is_valid_course_schedule(n: int, prerequisites: list[list[int]]) -> bool:
    def find_indegree():
        indegree = {i: 0 for i in range(n)}  # dict
        for pre in prerequisites:
            dep_course = pre[1]
            indegree[dep_course] += 1
        return indegree

    q = deque()
    indegree = find_indegree()
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)

    if len(q) <= 0:
        return False

    processed = 0

    while len(q) > 0:
        course = q.popleft()

        for pre in prerequisites:
            if pre[0] != course:
                continue
            indegree[pre[1]] -= 1
            if indegree[pre[1]] == 0:
                q.append(pre[1])
        processed += 1

    return processed == n


n = 2
prerequisites = [[0, 1]]
assert is_valid_course_schedule(2, prerequisites)
print("✅")

n = 2
prerequisites = [[0, 1], [1, 0]]
assert not is_valid_course_schedule(2, prerequisites)
print("✅")
