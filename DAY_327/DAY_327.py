
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "added")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack.pop(), "removed")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:", self.stack)

    def is_empty(self):
        return len(self.stack) == 0


# Main program
s = Stack()

while True:
    print("\n--- STACK MANAGER ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = int(input("Enter element: "))
        s.push(item)

    elif choice == "2":
        s.pop()

    elif choice == "3":
        s.peek()

    elif choice == "4":
        s.display()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
