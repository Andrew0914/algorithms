class QueueWithPointer:
    def __init__(self):
        self.startPointer = 0
        self.endPointer = 0

    def set_queue(self, queue):
        self.queue = queue

    def insert(self, value: int):
        if not self.queue:
            raise ValueError("No queue")
        self.endPointer += 1
        self.queue.append(value)

    def remove(self):
        if not self.queue or self.startPointer >= self.endPointer:
            raise IndexError("Out of bounds")
        self.startPointer += 1

    def peek(self):
        if self.startPointer >= self.endPointer:
            raise IndexError("No more elements")
        return self.queue[self.startPointer]
