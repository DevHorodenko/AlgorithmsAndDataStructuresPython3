# Using collections.deque in Python
# This script demonstrates basic operations with the deque class from the collections module, including adding, removing, and iterating over elements.

from collections import deque

d = deque()
d.append(10)  # Add to the back
d.appendleft(5)  # Add to the front
d.append(15)  # Add to the back again
d.appendleft(0)  # Add to the front again

for i in d:
    print(i, end=' ')

print('/n')

d.pop()  # Remove from the back
d.popleft()  # Remove from the front

for i in d:
    print(i, end=' ')

print('/n')

d.remove(5)  # Remove the first occurrence of 5

for i in d:
    print(i, end=' ')