class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "added to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack.pop(), "removed from stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Current Stack:", self.stack)

    def is_empty(self):
        return len(self.stack) == 0


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()

s.pop()

s.display()
s.peek()

print("Is stack empty?", s.is_empty())
