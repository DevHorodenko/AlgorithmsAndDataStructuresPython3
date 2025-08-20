# Hash Table Implementation in Python
# This implementation uses chaining for minimal collision resolution example.

import sys

class HashTable:

    def __init__(self, size):
        """Initialize the hash table with a given size."""
        if size < 1:
            raise ValueError("Size must be a positive integer.")
            sys.exit(1)
        
        self.size = size
        self.table = [[] for i in range(size)]

    def hash(self, key):
        """Compute the hash value for a given key."""
        return key % self.size

    def insert(self, key):
        """Insert a key into the hash table."""
        self.table[self.hash(key)].append(key)

    def show(self):
        """Display the contents of the hash table."""
        for list in self.table:
            if list:
                for item in list:
                    print('%d' % item, end=' ')
                print('')

    def search(self, key):
        """Search for a key in the hash table."""
        if key in self.table[self.hash(key)]:
            print("Key %d found in the hash table." % key)
            return True
        else:
            print("Key %d not found in the hash table." % key)
            return False
        
# Example usage:
d = HashTable(9)
d.insert(19)
d.insert(28)
d.insert(20)
d.insert(5)
d.insert(33)
d.insert(15)

d.show() # Display the contents of the hash table