class Stack:
    def __init__(self):
        self.stack = []
        self.pointer = 0

    def push(self, item):
        self.stack.append(item)
        self.pointer += 1

    def pop(self):
        if len(self.stack)  <= 0:
            print("Stack is empty")
        else:
            self.stack.pop()
            self.pointer -= 1

    def peek(self):
        if len(self.stack)  <= 0:
            print("Stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return self.pointer

    def log(self):
        print(self.stack)
