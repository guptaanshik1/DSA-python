import queueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
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
    return rootNode

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=' ')
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def iterativePreorder(rootNode):
    if rootNode is None: return
    stack = []
    stack.append(rootNode)
    while stack:
        current = stack.pop()
        print(current.data, end = ' ')

        if current.rightChild:
            stack.append(current.rightChild)
        if current.leftChild:
            stack.append(current.leftChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=' ')
    inOrderTraversal(rootNode.rightChild)

def iterativeInorder(rootNode):
    if not rootNode: return
    stack, current = [], rootNode
    while True:
        if current:
            stack.append(current)
            current = current.leftChild# reaching left most node
        elif stack:
            current = stack.pop()
            print(current.data, end = ' ')
            current = current.rightChild
        else:
            break

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=' ')

def iterativePostorder1(rootNode):
    if not rootNode: return
    recursiveStack, resultStack = [], []
    recursiveStack.append(rootNode)
    while recursiveStack:
        current = recursiveStack.pop()
        resultStack.append(current)
        if current.leftChild:
            recursiveStack.append(current.leftChild)
        if current.rightChild:
            recursiveStack.append(current.rightChild)
        
    while resultStack:
        current = resultStack.pop()
        print(current.data, end = ' ')

def iterativePostorder2(rootNode):
    if rootNode is None: return
    stack, prev = [], None
    stack.append(rootNode)
    
    while stack:
        curr = stack[-1]
        if prev is None or prev.leftChild == curr or prev.rightChild == curr:
            if curr.leftChild:
                stack.append(curr.leftChild)
            elif curr.rightChild:
                stack.append(curr.rightChild)
            else:
                print(curr.data, end = ' ')
                stack.pop()

        elif prev == curr.leftChild:
            if curr.rightChild:
                stack.append(curr.rightChild)
        else:
            print(curr.data)
            stack.pop()

        prev = curr
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data, end=' ')
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The node has been found successfully")
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild == nodeValue:
            print("The node has been found successfully")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    elif nodeValue >= rootNode.data:
        if rootNode.rightChild == nodeValue:
            print("The node has been found successfully")
        else:
            searchNode(rootNode.rightChild, nodeValue)
    else:
        print("The node has not been found")

def getSuccessor(rootNode):
    current = rootNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

def predecessor(rootNode):
    current = rootNode.rightChild
    while current.rightChild:
        current = current.rightChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:# if there is only one child then assign the child of node to be deleted to the parent of node to be deleted
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp#returning rightChild
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp#returning leftChild
        temp = getSuccessor(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)# temp will be deleted by calling delete function recursively for for right subtree and deleting temp value
        """
        if not (rootNode.leftChild or root.rightChild): # if a leaf node
            rootNode = None

        elif rootNode.right: # only right is present
            rootNode.data = successor(rootNode)
            rootNode.rightChild = deleteNode(rootNode.rightChild, rootNode.data)

        else:# only left is present
            rootNode.data = predecessor(rootNode)
            rootNode.leftChild = deleteNode(rootNode.leftChild, rootNode.data)
        """
    return rootNode

def countLeafNodes(root):
    if root is None: return 0
    if root.leftChild is None and root.rightChild is None:
        return 1
    else:
        return countLeafNodes(root.leftChild) + countLeafNodes(root.rightChild)

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"

# newBST = BSTNode(70)
# insertNode(newBST, 90)
# insertNode(newBST, 50)
# insertNode(newBST, 30)
# insertNode(newBST, 40)
# insertNode(newBST, 80)
# insertNode(newBST, 100)

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

print()
print("Iterative Preorder: ")
iterativePreorder(newBST)

print()
print("Iterative Inorder: ")
iterativeInorder(newBST)

print()
print("Iterative Postorder 1: ")
iterativePostorder1(newBST)

print()
print("Iterative Postorder 2: ")
iterativePostorder2(newBST)

print()
print("Number of leaf nodes are: ", countLeafNodes(newBST))

# searchNode(newBST, 100)
# searchNode(newBST, 120)

# print(getSuccessor(newBST))
# deleteNode(newBST, 100)

print()

# print(deleteBST(newBST))
# levelOrderTraversal(newBST)