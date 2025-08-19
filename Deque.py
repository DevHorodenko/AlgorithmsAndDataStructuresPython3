# Double Ended Queue Implementation
# This implementation provides a basic double-ended queue (deque) with methods to add and remove elements from both ends.

class Deque:
    def __init__(self):
        self.items = []
        self.len = 0

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0
    
    def push_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)
        self.len += 1

    def push_back(self, item):
        """Add an item to the back of the deque."""
        self.items.insert(self.len, item)
        self.len += 1

    def pop_front(self):
        """Remove and return the item from the front of the deque."""
        if self.is_empty():
            raise IndexError("pop_front from empty deque")
        item = self.items.pop(0)
        self.len -= 1
        return item
    
    def pop_back(self):
        """Remove and return the item from the back of the deque."""
        if self.is_empty():
            raise IndexError("pop_back from empty deque")
        item = self.items.pop()
        self.len -= 1
        return item
    
    def peek_front(self):
        """Return the item at the front of the deque without removing it."""
        if self.is_empty():
            raise IndexError("peek_front from empty deque")
        return self.items[0]
    
    def peek_back(self):
        """Return the item at the back of the deque without removing it."""
        if self.is_empty():
            raise IndexError("peek_back from empty deque")
        return self.items[-1]
    
    def show(self):
        """Return a list of items in the deque."""
        return self.items.copy()

d = Deque()

# Insert
d.push_front(10)
d.push_back(5)
print(d.show())  # Output: [10, 5]
d.push_front(20)
print(d.show()) # Output: [20, 10, 5]
d.push_back(30)
print(d.show()) # Output: [20, 10, 5, 30]
print('Front : %d' % d.peek_front())  # Output Front : 20
print('Back : %d' % d.peek_back())  # Output Back : 30

# Remove
d.pop_back()
print(d.show())  # Output: [20, 10, 5]
d.pop_front()
print(d.show())  # Output: [10, 5]