# Stack Data Structure Implementation
# This module provides a basic stack implementation with methods to push, pop, and inspect elements.

class Stack:

    def __init__(self):
        self.stack = [] # Initialize a void stack
        pass

    def push(self, element):
        self.stack.append(element) # Adds element to stack

    def pop(self):
        if not(self.isEmpty): # Check if the length of the stack is not empty
            self.stack.pop(len(self.stack - 1)) # Removes last element in the stack

    def top(self):
        if not(self.isEmpty): # Check if the length of the stack is not empty
            return self.stack[-1] # Return the last element in the stack
        return None
    
    def isEmpty(self):
        if(len(self.stack) == 0): # Check if the length of the stack is empty
            return True
        return False