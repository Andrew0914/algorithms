class StackWithPointer:
    def __init__(self):
        self.stack = []
        # Top pointer -1 means empty stack
        self.top = -1

    def push(self, item: int):
        self.stack.append(item)
        self.top += 1
        return item


    def pop(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        self.top -= 1
        removed = self.stack.pop()
        return removed

    def peek(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    def clear(self):
        self.stack.clear()
        self.top = -1
