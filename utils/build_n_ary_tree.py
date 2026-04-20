from collections import deque
from utils.n_ary_node import NAryNode


def build_n_ary_tree(data: list) -> "NAryNode | None":
    if not data:
        return None

    root = NAryNode(data[0], [])
    queue = deque([root])
    i = 2  # skip root value and first null separator

    while i < len(data) and queue:
        parent = queue.popleft()
        while i < len(data) and data[i] is not None:
            child = NAryNode(data[i], [])
            parent.children.append(child)
            queue.append(child)
            i += 1
        i += 1  # skip the null separator

    return root
