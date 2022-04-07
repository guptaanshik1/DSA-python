class Heap:
    def __init__(self, size):
        self.customList = [None] * (size + 1)
        self.heapSize = 0
        self.maxSize = size + 1

def peakofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return "There is no node to traverse"
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min" or heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    if heapType == "Max" or heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The node has been succesfully inserted in the binary heap"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = (index * 2) + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
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
                swapChild = leftIndex
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

        heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return "The binary heap is empty"
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return "The node has been successfully extracted from the binary heap"

newMinHeap = Heap(8)
newMaxHeap = Heap(5)

print("Min Heap before extraction:")
insertNode(newMinHeap, 5, "Min")
insertNode(newMinHeap, 30, "Min")
insertNode(newMinHeap, 20, "Min")
insertNode(newMinHeap, 10, "Min")
insertNode(newMinHeap, 60, "Min")
insertNode(newMinHeap, 50, "Min")
insertNode(newMinHeap, 40, "Min")
insertNode(newMinHeap, 80, "Min")

levelOrderTraversal(newMinHeap)

extractNode(newMinHeap, "Min")
print("Min Heap after extraction:")
levelOrderTraversal(newMinHeap)

print("Max Heap before extraction:")
insertNode(newMaxHeap, 4, "Max")
insertNode(newMaxHeap, 5, "Max")
insertNode(newMaxHeap, 2, "Max")
insertNode(newMaxHeap, 1, "Max")

levelOrderTraversal(newMaxHeap)

extractNode(newMaxHeap, "Max")
print("Max Heap after extraction:")
levelOrderTraversal(newMaxHeap)