from collections import deque

queue = deque()

queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(4)
print(queue)

queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

