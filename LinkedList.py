# Singly Linked List Implementation in Python
# This module provides a basic singly linked list with methods to insert, remove, and display elements, as well as check size and emptiness of the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNext(self):
        return self.next
    
    def setNext(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def show(self):
        if self.isEmpty():
            return "List is empty"
        else:
            current = self.head
            elements = []
            while current is not None:
                elements.append(current.getData())
                current = current.getNext()
            return " -> ".join(map(str, elements))
    
    def push(self, data, index):
        if index >= 0:
            new_node = Node(data)
            if self.isEmpty():
                self.head = new_node
                self.last = new_node
            else:
                if index == 0:
                    new_node.setNext(self.head)
                    self.head = new_node
                elif index >= self.size:
                    self.last.setNext(new_node)
                    self.last = new_node
                else:
                    previous = self.head
                    current = self.head.getNext()
                    currIndex = 1
                    while current != None:
                        if currIndex == index:
                            new_node.setNext(current)
                            previous.setNext(new_node)
                            break
                        previous = current
                        current = current.getNext()
                        currIndex += 1
            self.size += 1
        else:
            raise IndexError("Index must be a non-negative integer")
        
    def pop(self, index):
        if self.isEmpty():
            raise IndexError("List is empty")
        if index >= 0 and index < self.size:
            flag_remove = False
            if self.head.getNext() == None:
                self.head = None
                self.last = None
                flag_remove = True
            elif index == 0:
                self.head = self.head.getNext()
                flag_remove = True
            else:
                previous = self.head
                current = self.head.getNext()
                currIndex = 1

                while current != None:
                    if currIndex == index:
                        previous.setNext(current.getNext())
                        current.setNext(None)
                        flag_remove = True
                        break
                    previous = current
                    current = current.getNext()
                    currIndex += 1
            if flag_remove:
                self.size -= 1
        else:
            raise IndexError("Index out of bounds")
        
list = LinkedList()

list.push('Leo', 0)
print(list.show())  # Should show "Leo"

list.push('Jhon', 1)
print(list.show())  # Should show "Leo -> Jhon"

list.push('Mary', 0)
print(list.show())  # Should show "Mary -> Leo -> Jhon"

list.push('Joseph', 2)
print(list.show())  # Should show "Mary -> Leo -> Joseph -> Jhon"

list.push('Jordan', 4)
print(list.show())  # Should show "Mary -> Leo -> Joseph -> Jhon -> Jordan"

list.push('Gragas', 2)
print(list.show())  # Should show "Mary -> Leo -> Gragas -> Joseph -> Jhon -> Jordan"

print("List size: " + str(list.getSize()))  # Should show "List size: 6"

list.pop(0)
print(list.show())  # Should show "Leo -> Gragas -> Joseph -> Jhon -> Jordan"

list.pop(2)
print(list.show())  # Should show "Leo -> Gragas -> Jhon -> Jordan"

list.pop(3)
print(list.show())  # Should show "Leo -> Gragas -> Jhon"

print("List size: " + str(list.getSize()))  # Should show "List size: 3"