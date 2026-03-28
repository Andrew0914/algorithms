from utils.dbl_node import DblNode


class DblLinkedList:
    def __init__(
        self, first_node: "DblNode | None" = None, last_node: "DblNode | None" = None
    ):
        self.head = first_node
        self.tail = last_node

    def insert_at_end(self, value):
        new_node = DblNode(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.tail

        if self.tail is None:
            self.tail = new_node
            return self.tail

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display_as_array(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result


sue = DblNode(value="Sue")
greg = DblNode(value="Greg")
bob = DblNode(value="Bob")

sue.next = greg
greg.prev = sue
greg.next = bob
bob.prev = greg

dbl_list = DblLinkedList(first_node=sue, last_node=bob)
dbl_list.insert_at_end("Daniela")
print(dbl_list.display_as_array())
