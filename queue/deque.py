from collections import deque

queue = deque()

print('=== append')
queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(4)
print(queue)
print('=== popleft / pop ')
queue.popleft()
# queue.pop()
print(queue)

queue.popleft()
# queue.pop()
print(queue)

queue.popleft()
# queue.pop()
print(queue)

