class DequeueWithPointer:
    def __init__(self):
        self.front_pointer = 0
        self.back_pointer = 0
        self.queue = []

    def push_front(self, item):
        self.back_pointer += 1
        self.queue.insert(self.front_pointer, item)

    def push_back(self, item):
        self.queue.insert(self.back_pointer, item)
        self.back_pointer += 1

    def pop_back(self):
        if self.back_pointer < 0:
            raise IndexError("Queue is empty")
        removed = self.queue.pop(self.back_pointer - 1)
        self.back_pointer -= 1
        return removed

    def pop_front(self):
        if self.back_pointer < 0:
            raise IndexError("Queue is empty")
        removed = self.queue.pop(self.front_pointer)
        self.back_pointer -= 1
        return removed

    def peek_front(self):
        if self.front_pointer == self.back_pointer:
            raise IndexError("Queue is empty")
        return self.queue[self.front_pointer]

    def peek_back(self):
        if self.front_pointer == self.back_pointer:
            raise IndexError("Queue is empty")
        return self.queue[self.back_pointer - 1]

    def log(self):
        print(f"frontPointer: {self.front_pointer}, backPointer: {self.back_pointer}")
        print(self.queue)
