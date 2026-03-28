from __future__ import annotations

from collections import deque


class Person:
    def __init__(self, name):
        self.name = name
        self.friends: list[Person] = []
        self.visited = False

    def add_friend(self, friend: Person) -> list[Person]:
        self.friends.append(friend)
        return self.friends

    def __repr__(self) -> str:
        return self.name

    def display_network(self):
        visited: set[Person] = {self}
        queue: deque[Person] = deque([self])

        while queue:
            print(queue)
            current_vertex = queue.popleft()
            # print(current_vertex.name)

            unvisited = [f for f in current_vertex.friends if f not in visited]
            visited.update(unvisited)
            queue.extend(unvisited)


mary = Person("Mary")
jose = Person("Jose")
rita = Person("Rita")
andrew = Person("Andrew")

mary.add_friend(jose)
jose.add_friend(mary)
mary.add_friend(andrew)
andrew.add_friend(rita)

mary.display_network()
