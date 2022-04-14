from collections import deque

d = deque()

d.append(1)
d.append(2)

print(d)

d.appendleft('3')
print(d)
d.append(4)
print(d)

d.popleft()
print(d)
d.pop()
print(d)

d.extend([12, 6, 7, 8, 9])
print(d)
d.extendleft([55, 23])
print(d)
d.clear()
print(d)
d.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(d)
d.rotate()
print(d)
