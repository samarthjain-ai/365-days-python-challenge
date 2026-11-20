class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "added")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(self.stack.pop(), "removed")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()
s.peek()

print("Stack:", s.stack)