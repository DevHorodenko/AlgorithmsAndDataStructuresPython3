# Binary Search Tree Implementation in Python
# This module provides a basic binary search tree (BST) with methods to insert nodes, check size and emptiness, and display elements in pre-order.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def getLeftChild(self):
        return self.leftChild
    
    def setLeftChild(self, left_child):
        self.leftChild = left_child

    def getRightChild(self):
        return self.rightChild
    
    def setRightChild(self, right_child):
        self.rightChild = right_child

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def getRoot(self):
        """Return the root node of the tree."""
        return self.root

    def isEmpty(self):
        """Check if the tree is empty."""
        return self.size == 0
    
    def getSize(self):
        """Return the number of nodes in the tree."""
        return self.size
    
    def showInPreOrder(self, current):
        """Return a list of elements in the tree in sorted order."""
        if current != None:
            print('%d' % current.getData(), end=' ')
            self.showInPreOrder(current.getLeftChild())
            self.showInPreOrder(current.getRightChild())

    def insert(self, data):
        """Insert a new node with the given data into the tree."""
        new_node = Node(data)

        if self.isEmpty():
            self.root = new_node
            self.size += 1
            return
        else:
            dadNode = None
            current = self.root
            while current is not None:
                dadNode = current

                if data < current.getData():
                    current = current.getLeftChild()
                elif data > current.getData():
                    current = current.getRightChild()
                else:
                    return
            if data < dadNode.getData():
                dadNode.setLeftChild(new_node)
            else:
                dadNode.setRightChild(new_node)
            self.size += 1
            return
                
    def pop(self, data):
        """Remove a node with the given data from the tree."""
        if self.isEmpty():
            raise ValueError("Tree is empty, cannot pop.")
        dadNode = None
        current = self.root

        while current is not None:
            if data == current.getData():
                # Case 1: No children
                if current.getLeftChild() is None and current.getRightChild() is None:
                    if dadNode is None:
                        self.root = None
                    else:
                        if dadNode.getLeftChild() == current:
                            dadNode.setLeftChild(None)
                        elif dadNode.getRightChild() == current:
                            dadNode.setRightChild(None)
                    self.size -= 1
                    break

                # Case 2: One child
                elif (current.getLeftChild() is None) != (current.getRightChild() is None):
                    child = current.getLeftChild() if current.getLeftChild() else current.getRightChild()
                    if dadNode is None:
                        self.root = child
                    else:
                        if dadNode.getLeftChild() == current:
                            dadNode.setLeftChild(child)
                        else:
                            dadNode.setRightChild(child)
                    self.size -= 1
                    break

                # Case 3: Two children
                else:
                    # Find the inorder successor (smallest in the right subtree)
                    dadSmallerNode = current
                    smallerNode = current.getRightChild()
                    while smallerNode.getLeftChild() is not None:
                        dadSmallerNode = smallerNode
                        smallerNode = smallerNode.getLeftChild()

                    # Replace current's data with successor's data
                    current.setData(smallerNode.getData())
                    # Now remove the successor node
                    if dadSmallerNode.getLeftChild() == smallerNode:
                        dadSmallerNode.setLeftChild(smallerNode.getRightChild())
                    else:
                        dadSmallerNode.setRightChild(smallerNode.getRightChild())
                    self.size -= 1
                    break

            dadNode = current
            if data < current.getData():
                current = current.getLeftChild()
            else:
                current = current.getRightChild()
        return

tree = BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
tree.insert(13)
print(tree.showInPreOrder(tree.getRoot())) # Output: 8 3 1 6 4 7 10 14 13
print("\nSize of the tree:", tree.getSize()) # Output: Size of the tree: 9

tree.pop(8)
print(tree.showInPreOrder(tree.getRoot())) # Output: 10 3 1 6 4 7 14 13
print("\nSize of the tree after pop:", tree.getSize()) # Output: Size of the tree after pop: 8