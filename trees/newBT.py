import queueLinkedList as queue

class BTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# def insertNode(rootNode, nodeValue):
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    postOrderTraversal(rootNode.rightChild)

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
            print(root.data)
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            else:
                root.leftChild = nodeValue
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
            else:
                root.rightChild = nodeValue

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == nodeValue:
                return "The node has been found in the tree successfully"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "The node has not been found in the tree"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return root
                    
def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.leftChild:
                if root.leftChild is deepestNode:
                    root.leftChild = None
                else:
                    customQueue.enqueue(root.leftChild)
            if root.rightChild:
                if root.rightChild is deepestNode:
                    root.rightChild = None
                else:
                    customQueue.enqueue(root.rightChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            deepestNode = getDeepestNode(rootNode)
            if root.data == nodeValue:
                root.data = deepestNode.data
                deleteDeepestNode(rootNode, deepestNode)
                return "The node has been deleted successfully"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "The node has not been deleted"
                
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary tree has been deleted successfully"

newBT = BTNode("Drinks")
hot = BTNode("Hot")
cold = BTNode("Cold")
newBT.leftChild = hot
newBT.rightChild = cold

print("Pre Order:")
preOrderTraversal(newBT)
print()
print("In Order:")
inOrderTraversal(newBT)
print()
print("Post Order:")
postOrderTraversal(newBT)
print()
print("Level Order:")
levelOrderTraversal(newBT)
print()
print(searchNode(newBT, "Fanta"))

# print(getDeepestNode(newBT))
# deepestNode = getDeepestNode(newBT)
# print(deleteDeepestNode(newBT, deepestNode))
print(deleteNode(newBT, "Drinks"))
preOrderTraversal(newBT)
# print(deleteBT(newBT))
# preOrderTraversal(newBT)