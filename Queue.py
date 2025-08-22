# Queue Data Structure Implementation
# This module provides a basic queue implementation with methods to enqueue, dequeue, and inspect elements.

class Queue:

    def __init__(self):
        self.queue = []
        self.length = 0
    
    def push(self, item):
        self.queue.append(item)
        self.length += 1
    
    def pop(self):
        if self.size(self) == 0:
            raise IndexError("pop from empty queue")
        item = self.queue.pop(0)
        self.length -= 1
        return item
    
    def size(self):
        return self.len_queue

    def front(self):
        if self.size() != 0:
            return self.queue[0]
        return None