from utils.node import Node


class LinkedList:
    def __init__(self, node: Node):
        self.head = node

    def at(self, index: int) -> "Node | None":
        current_index = 0
        node: Node | None = self.head
        while current_index < index:
            if node is None:
                return None
            node = node.next
            current_index += 1
        return node

    def search(self, value) -> tuple[int, "Node | None"]:
        index = 0
        node = None
        current = self.head
        while current:
            if current.value == value:
                node = current
                break
            index += 1
            current = current.next

        return -1 if node is None else index, node

    def len(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert_at(self, index: int, value) -> Node:
        node = Node(value=value)
        # At the beggining
        if index == 0:
            node.next = self.head
            self.head = node
            return node

        prev_node = self.at(index - 1)

        if prev_node is None:
            raise IndexError("Index out of range")

        prev_node.next, node.next = node, prev_node.next

        return node

    def delete_at(self, index: int) -> "Node | None":
        if index == 0:
            self.head = self.head.next if self.head else None
            return self.head

        prev_node = self.at(index - 1)

        if prev_node is None or prev_node.next is None:
            raise IndexError("Index out of range")

        deleted = prev_node.next
        prev_node.next = deleted.next

        return deleted

    def display(self) -> None:
        current = self.head
        like_array = []
        while current:
            like_array.append(current.value)
            current = current.next
        print(like_array)


node = Node(1)
node2 = Node(2)
node3 = Node(3)
node.next = node2
node2.next = node3

ll = LinkedList(node)
ll.insert_at(3, 4)
ll.insert_at(4, 5)
ll.display()
ll.delete_at(0)
ll.display()
