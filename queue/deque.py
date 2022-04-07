from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

queue.appendleft(5)
queue.appendleft(6)
print(queue)

queue.rotate(2)

print(queue)