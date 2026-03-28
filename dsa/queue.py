class Queue:
    def __init__(self):
        self.queue = []

    def set_queue(self, items):
        self.queue = items

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) <= 0:
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) <= 0:
            return None
        else:
            return self.queue[0]

    def log(self):
        print(self.queue)
