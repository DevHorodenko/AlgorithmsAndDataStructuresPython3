class OptimizedStack:

    def __init__(self):
        self.optimizedStack = [] # Initialize a void stack
        self.lenStack = 0 # Initialize stack size for optimized functions
        pass

    def push(self, element):
        self.optimizedStack.append(element) # Adds element to stack
        self.lenStack += 1 # Increment stack size

    def pop(self):
        if not(self.isEmpty): # Check if the length of the stack is not empty
            self.optimizedStack.pop(len(self.lenStack - 1)) # Removes last element in the stack
            self.lenStack -= 1 # Decrease stack size
    def top(self):
        if not(self.isEmpty): # Check if the length of the stack is not empty
            return self.optimizedStacks[-1] # Return the last element in the stack
        return None
    
    def isEmpty(self):
        if(self.lenStack == 0): # Check if the length of the stack is empty
            return True
        return False
    
    def length(self):
        return self.lenStack # Get size of the stack