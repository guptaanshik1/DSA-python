class BinaryTree:
    def __init__(self, maxSize):
        self.customList = maxSize * [None]
        self.lastUsedIndex = 0#1st index is not taken
        self.maxSize = maxSize

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been inserted successfully"

    def preOrderTraversal(self, root):
        if self.customList == None:
            return "There are no nodes to traverse in the tree"
        if root > self.lastUsedIndex:
            return
        else:
            print(self.customList[root])
            self.preOrderTraversal(root * 2)
            self.preOrderTraversal(root * 2 + 1)

    def inOrderTraversal(self, root):
        if self.customList == None:
            return "There are no nodes to traverse in the tree"
        if root > self.lastUsedIndex:
            return
        self.inOrderTraversal(root * 2)
        print(self.customList[root])
        self.inOrderTraversal(root * 2 + 1)

    def postOrderTraversal(self, root):
        if self.customList == None:
            return "There are no nodes to traverse in the tree"
        if root > self.lastUsedIndex:
            return
        self.postOrderTraversal(root * 2)
        self.postOrderTraversal(root * 2 + 1)
        print(self.customList[root])

    def levelOrderTraversal(self, root):
        if self.customList == None:
            return "There are no nodes to traverse in the tree"
        for i in range(root, self.lastUsedIndex + 1):
            print(self.customList[i])
        # for i in range(len(self.customList)):
        #     print(self.customList[i])
        
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if nodeValue == self.customList[i]:
                return "The node has been found successfully"
        return "The node has not been found"

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is no node to delete"
        else:
            for i in range(len(self.customList)):
                if value == self.customList[i]:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    return "The node has been deleted successfully"

    def deleteBT(self):
        self.customList = None
        return "The tree has been deleted successfully"

newBT = BinaryTree(8)

newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.insertNode("Cold")

print("Pre Order:")
newBT.preOrderTraversal(1)
print()
print("In Order:")
newBT.inOrderTraversal(1)

print()
print("Post Order:")
newBT.postOrderTraversal(1)

print()
print("Level Order:")
newBT.levelOrderTraversal(1)

print()
print(newBT.searchNode("Tea"))
print(newBT.searchNode("Fanta"))

print()
print(newBT.deleteNode("Tea"))

print()
print("Level Order:")
newBT.levelOrderTraversal(1)

print()
print(newBT.deleteBT())

print("Level Order:")
newBT.levelOrderTraversal(1)