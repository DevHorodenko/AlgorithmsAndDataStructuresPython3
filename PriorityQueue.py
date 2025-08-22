# Priority Queue Implementation in Python
# This module provides a basic priority queue with methods to insert/remove persons based on their priority, check size and emptiness, and display all persons in the queue.

class Person:

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def getName(self):
        return self.name
    
    def getPriority(self):
        return self.priority
    
    def setName(self, name):
        self.name = name

    def setPriority(self, priority):
        self.priority = priority

class PriorityQueue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def isEmpty(self):
        """Check if the priority queue is empty."""
        if self.size == 0:
            return True
        return False
    
    def getSize(self):
        """Return the number of elements in the priority queue."""
        return self.size
    
    def push(self, person):
        """Insert a new person into the priority queue based on their priority."""
        
        flagPush = False

        if self.isEmpty():
            self.queue.append(person)
            flagPush = True
            self.size += 1
        else:
            for i in range(self.size):
                if self.queue[i].getPriority() < person.getPriority():
                    self.queue.insert(i, person)
                    flagPush = True
                    self.size += 1
                    break
            if not flagPush:
                self.queue.insert(self.size, person)
                self.size += 1
    
    def pop(self):
        """Remove and return the person with the highest priority from the queue."""

        if not self.isEmpty():
            self.queue.pop(0)
            self.size -= 1
    
    def show(self):
        """Display all persons in the priority queue."""

        for person in self.queue:
            print(f'Name: {person.getName()}, Priority: {person.getPriority()}')

# Example usage:
pq = PriorityQueue()
pq.push(Person("Alice", 25))
pq.push(Person("Bob", 50))
pq.push(Person("Charlie", 30))

pq.show()
print("Size of the priority queue:", pq.getSize())  # Output: Size of the priority queue: 3

pq.pop()
print("After popping the highest priority person:")
pq.show()
print("Size of the priority queue:", pq.getSize())  # Output: Size of the priority queue: 2