from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

removed = queue.popleft()
print("Removed:", removed)

print("Updated Queue:", queue)