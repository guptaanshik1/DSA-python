class Heap:
    def __init__(self, size):
        self.customList = [None] * (size + 1)
        self.heapSize = 0#size in the beginning
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return "The binary heap is empty"
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        print("There is no node in the heap to traverse")
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min" or heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = rootNode.customList[index]
            rootNode.customList[index] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)

    if heapType == "Max" or heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = rootNode.customList[index]
            rootNode.customList[index] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue#heapSize is current cell and heapSize + 1 is the next cell
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The node has been successfully inserted in the binary heap"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = (index * 2) + 1
    swapChild = 0
    
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:#if root has only one child
        if heapType == "Min" or heapType == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        elif heapType == "Max" or heapType == "max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            return
        
    else:
        if heapType == "Min" or heapType == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex#selecting smaller in the case of min heap
            else:
                swapChild = rightIndex
            
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp

        elif heapType == "Max" or heapType == "max":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = rightIndex
            else:
                swapChild = leftIndex
            
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp

        else:
            return

    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        print("There is no node in the binary heap to extract")
    extractedNode = rootNode.customList[1]#rootNode
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]#rootNode.heapsize represents the last node
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)

def deleteBH(rootNode):
    rootNode.customList = None
    print("The binary heap has been deleted successfully")
    
newMinHeap = Heap(8)

# print(peekofHeap(newHeap))
# print(sizeofHeap(newHeap))
print("Min Heap: ")
insertNode(newMinHeap, 5, "Min")
insertNode(newMinHeap, 30, "Min")
insertNode(newMinHeap, 20, "Min")
insertNode(newMinHeap, 10, "Min")
insertNode(newMinHeap, 60, "Min")
insertNode(newMinHeap, 50, "Min")
insertNode(newMinHeap, 40, "Min")
insertNode(newMinHeap, 80, "Min")

levelOrderTraversal(newMinHeap)
print("After extraction min heap:")
extractNode(newMinHeap, "Min")
levelOrderTraversal(newMinHeap)

newMaxHeap = Heap(5)

print("Max Heap: ")
insertNode(newMaxHeap, 4, "Max")
insertNode(newMaxHeap, 5, "Max")
insertNode(newMaxHeap, 2, "Max")
insertNode(newMaxHeap, 1, "Max")

levelOrderTraversal(newMaxHeap)
print("After extraction max heap:")
extractNode(newMaxHeap, "Max")
levelOrderTraversal(newMaxHeap)

deleteBH(newMinHeap)
deleteBH(newMaxHeap)

levelOrderTraversal(newMaxHeap)
levelOrderTraversal(newMinHeap)