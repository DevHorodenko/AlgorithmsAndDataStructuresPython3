# Binary Heap Implementation in Python
# This module provides a basic binary heap with methods to insert and remove elements, check size and emptiness, and display elements in sorted order.
# Module heapq is used for heap operations.

import heapq

class Person:

    def __init__(self, name, age):
        """Initialize a person with a name and age."""
        self.name = name
        self.age = age # Age will be used as the priority for the heap.

    def __repr__(self):
        """Return a string representation of the person."""
        return f"Person(name={self.name}, age={self.age})"

    def __lt__(self, other):
        """Define less than for comparing persons based on age."""
        return self.age < other.age
    
class BinaryHeap:
    """A simple binary heap implementation using a list."""

    def __init__(self):
        """Initialize an empty binary heap."""
        self.queue = []
        self.index = 0
        self.size = 0

    def insert(self, person):
        """Insert a person into the binary heap."""
        heapq.heappush(self.queue, (-person.age, self.index, person))  # Use negative age for max-heap behavior
        self.index += 1
        self.size += 1

    def pop(self):
        """Remove and return the person with the highest priority from the heap."""
        if not self.isEmpty():
            self.size -= 1
            return heapq.heappop(self.queue)[-1]
        return None

    def isEmpty(self):
        """Check if the binary heap is empty."""
        return self.size == 0
    
queue = BinaryHeap()

queue.insert(Person("Mary", 20))
queue.insert(Person("Peter", 16))
queue.insert(Person("Felipe", 25))
queue.insert(Person("Carol", 23))

print("Queue size:", queue.size)

print(queue.pop())  # Should remove and return the person with the highest priority (oldest)
print("Queue size after pop:", queue.size)