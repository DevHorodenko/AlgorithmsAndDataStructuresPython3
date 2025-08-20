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
                
    def pop(self, data):
        """Remove a node with the given data from the tree."""
        if self.isEmpty():
            raise ValueError("Tree is empty, cannot pop.")
        """ Case 1: when the node doesnt have children """
        """ Case 2: when the node has one child """
        """ Case 3: when the node has two children """
        dadNode = None
        current = self.root

        while current is not None:
            # Check if node to be deleted is found
            if data == current.getData():
                # Case 1
                if current.getLeftChild() == None and current.getRightChild() == None:
                    # If the node is the root
                    if dadNode is None:
                        self.root = None
                    else:
                        # Check if the node is a left or right child
                        if dadNode.getLeftChild() == current:
                            dadNode.setLeftChild(None)
                        elif dadNode.getRightChild() == current:
                            dadNode.setRightChild(None)
                # Case 2
                elif (current.getLeftChild() == None and current.getRightChild() != None) or (current.getRightChild() == None and current.getLeftChild() != None):
                    # If the node is the root
                    if dadNode is None:
                        if current.getLeftChild() is not None:
                            self.root = current.getLeftChild()
                        elif current.getRightChild() is not None:
                            self.root = current.getRightChild()
                        else:
                            self.root = None
                    else:
                        # Check if the node is a left or right child
                        if current.getLeftChild() is not None:
                            if dadNode.getLeftChild() and dadNode.getLeftChild().getData() == current.getData():
                                dadNode.setLeftChild(current.getLeftChild())
                            else:
                                dadNode.setRightChild(current.getLeftChild())
                        else:
                            if dadNode.getLeftChild() and dadNode.getLeftChild().getData() == current.getData():
                                dadNode.setLeftChild(current.getRightChild())
                            else:
                                dadNode.setRightChild(current.getRightChild())
                # Case 3
                elif current.getLeftChild() != None and current.getRightChild() != None:
                    # Find the inorder successor (smallest in the right subtree)
                    dadSmallerNode = current
                    smallerNode = current.getRightChild()
                    nextSmallerNode = current.getRightChild().getLeftChild()
                    while nextSmallerNode is not None:
                        dadSmallerNode = smallerNode
                        smallerNode = nextSmallerNode
                        nextSmallerNode = nextSmallerNode.getLeftChild()
                    # Check if the node to be deleted is the root
                    if dadNode is None:
                        if self.root.getRightChild().getData() == smallerNode.getData():
                            smallerNode.setLeftChild(self.root.getLeftChild())
                        else:
                            if dadSmallerNode.getLeftChild() and dadSmallerNode.getLeftChild().getData() == smallerNode.getData():
                                dadSmallerNode.setLeftChild(None)
                            else:
                                dadSmallerNode.setRightChild(None)
                            
                            smallerNode.setLeftChild(current.getLeftChild())
                            smallerNode.setRightChild(current.getRightChild())
                        self.root = smallerNode
                    else:
                        pass

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
print("\nSize of the tree:", tree.getSize())