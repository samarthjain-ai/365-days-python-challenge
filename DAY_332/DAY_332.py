
from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue.popleft(), "removed from queue")

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Current Queue:", list(self.queue))

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()

print("Is Queue Empty?", q.is_empty())
