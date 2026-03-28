class Node:
    def __init__(self, value, next: "Node | None" = None):
        self.value = value
        self.next = next
