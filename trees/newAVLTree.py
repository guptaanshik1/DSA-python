import queueLinkedList as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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
            print(root.data)
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    #LL condition
    if balance > 1 and rootNode.leftChild.data > nodeValue:
        return rightRotate(rootNode)

    #RR condition
    if balance < -1 and rootNode.rightChild.data < nodeValue:
        return leftRotate(rootNode)

    #LR condition
    if balance > 1 and rootNode.leftChild.data < nodeValue:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)

    #RL condition
    if balance < -1 and rootNode.rightChild.data > nodeValue:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return "There is no node in the AVL Tree"
    elif rootNode.data == nodeValue:
        return "The node has been found successfully"
    elif rootNode.data > nodeValue:
        if rootNode.leftChild.data == nodeValue:
            return "The node has been found successfully"
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            return "The node has been found successfully"
        else:
            searchNode(rootNode.rightChild, nodeValue)

def getSuccessor(rootNode):
    current = rootNode
    while current.leftChild:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getSuccessor(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightCHild = deleteNode(rootNode.rightChild, temp.data)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    #LL condition
    if balance > 1 and rootNode.leftChild.data > nodeValue:
        return rightRotate(rootNode)
    #RR condition
    if balance < -1 and rootNode.rightChild.data < nodeValue:
        return leftRotate(rootNode)
    #LR condition
    if balance > 1 and rootNode.leftChild.data < nodeValue:
        rootNode.leftChild = leftRotate(leftChild)
        return rightRotate(rootNode)
    #RL condition
    if balance < -1 and rootNode.rightChild.data > nodeValue:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL tree has been deleted successfully"

newAVL = AVLNode(30)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 25)
newAVL = insertNode(newAVL, 15)

print("Pre Order:")
preOrderTraversal(newAVL)
print()
print("In Order:")
inOrderTraversal(newAVL)

print()
print("Post Order:")
postOrderTraversal(newAVL)
print()
print(searchNode(newAVL, 15))
newAVL = deleteNode(newAVL, 20)
preOrderTraversal(newAVL)

print()
print(deleteAVL(newAVL))
preOrderTraversal(newAVL)