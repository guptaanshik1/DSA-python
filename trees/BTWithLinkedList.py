import queueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

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
                # print(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
                # print(root.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        rootNode = TreeNode(nodeValue)
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            else:
                root.leftChild = TreeNode(nodeValue)
                return "The node has been inserted successfully"
                
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
            else:
                root.rightChild = TreeNode(nodeValue)
                return "The node has been inserted successfully"

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return "The Binary Tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == nodeValue:
                return "The node has been found successfully"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "The node does not exist in the binary tree"

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
        deepestNode = root
        return deepestNode

def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return "There is no node in the binary tree"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            # if root.data == deepestNode:
            #     root.data = None
            #     return
            if root.rightChild:
                if root.rightChild is deepestNode:
                    root.rightChild = None
                    return "The deepest node has been deleted successfully"
                else:
                    customQueue.enqueue(root.rightChild)
            if root.leftChild:
                if root.leftChild is deepestNode:
                    root.leftChild = None
                    return "The deepest node has been deleted successfully"
                else:
                    customQueue.enqueue(root.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return "There is no node in the binary tree"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == nodeValue:
                deepestNode = getDeepestNode(rootNode)
                print("Deepest Node: ", deepestNode)
                root.data = deepestNode.data#replacing currentNode with deepestNode
                print(deleteDeepestNode(rootNode, deepestNode))#then deleting the deepestNode
                return "The node has been deleted successfully"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "The node does not exist in the binary tree"

def deleteBT(rootNode):
    if not rootNode:
        return
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary tree has been deleted successfully"

newBT = TreeNode(1)
hot = TreeNode("Hot")
cold = TreeNode("Cold")
newBT.leftChild = hot
newBT.rightChild = cold
fanta = TreeNode("Fanta")
cola = TreeNode("Cola")
cold.leftChild = fanta
cold.rightChild = cola
insertNode(newBT, 2)

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
print(searchNode(newBT, "Hot"))
print(searchNode(newBT, "Fizz"))
print()
# print("Deepest Node: ", getDeepestNode(newBT))

print()

deepestNode = getDeepestNode(newBT)

print(deleteNode(newBT, "Drinks"))

levelOrderTraversal(newBT)

print()
print(deleteBT(newBT))
levelOrderTraversal(newBT)