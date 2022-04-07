import queueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode == None:
        rootNode.data = BSTNode(nodeValue)
    elif rootNode.data > nodeValue:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been added successfully to the binary search tree"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(rootNode.data)
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        return "The node has been found successfully"
    elif rootNode.data >= nodeValue:
        if rootNode.leftChild == nodeValue:
            return "The node has been found successfully"
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == nodeValue:
            return "The node has been found successfully"
        else:
            searchNode(rootNode.rightChild, nodeValue)

def getSuccessor(rootNode):
    currentNode = rootNode
    while (currentNode.leftChild is not None):
        currentNode = currentNode.leftChild
    return currentNode

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return
    #leaf node
    elif rootNode.data > nodeValue:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif rootNode.data < nodeValue:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        #if 1 child is there
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode.data = temp
            temp = None
            return
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode.data = temp
            temp = None
            return
        
        temp = getSuccessor(rootNode)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The Binary Search Tree has been deleted successfully"

newBST = BSTNode(40)
insertNode(newBST, 30)
insertNode(newBST, 42)
insertNode(newBST, 5)
insertNode(newBST, 7)
insertNode(newBST, 23)
insertNode(newBST, 9)
insertNode(newBST, 19)

print("Pre Order:")
preOrderTraversal(newBST)
print()
print("In Order:")
inOrderTraversal(newBST)

print()
print("Post Order:")
postOrderTraversal(newBST)

print()
print("Level Order:")
levelOrderTraversal(newBST)

# print(searchNode(newBST, 90))
# deleteNode(newBST, 70)
# preOrderTraversal(newBST)

# print()
# print(deleteBST(newBST))
# preOrderTraversal(newBST)