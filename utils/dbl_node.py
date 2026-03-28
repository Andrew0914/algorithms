class DblNode:
    def __init__(
        self, value, prev: "DblNode | None" = None, next: "DblNode | None" = None
    ):
        self.value = value
        self.prev = prev
        self.next = next
