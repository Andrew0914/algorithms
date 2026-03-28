from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": ["bob"],
    "thom": [],
    "jonny": [],
}


def person_is_seller(name):
    return name[-1] == "m"


def search(graph, start):
    saerch_queue = deque()
    saerch_queue += graph[start]
    visited = set()

    while saerch_queue:
        person = saerch_queue.popleft()

        if person in visited:
            continue

        if person_is_seller(person):
            return person
        else:
            saerch_queue += graph[person]
        visited.add(person)

    return None


print(search(graph, "you"))
