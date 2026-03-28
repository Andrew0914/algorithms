class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, item):
        self.deque.insert(0, item)

    def push_back(self, item):
        self.deque.append(item)

    def pop_front(self):
        if len(self.deque) <= 0:
            print("Deque is empty")
        else:
            self.deque.pop(0)

    def pop_back(self):
        if len(self.deque) <= 0:
            print("Deque is empty")
        else:
            self.deque.pop()

    def peek_front(self):
        if len(self.deque) <= 0:
            print("Deque is empty")
        else:
            print(self.deque[0])

    def peek_back(self):
        if len(self.deque) <= 0:
            print("Deque is empty")
        else:
            print(self.deque[-1])

    def log(self):
        print(self.deque)
