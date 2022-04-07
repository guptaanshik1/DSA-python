from math import sqrt, ceil

def maximum(customList):
    max = 0
    for i in range(len(customList)):
        if customList[i] > max:
            max = customList[i]

    return max

def bubbleSort(customList):
    for i in range(len(customList)):
        for j in range(i + 1, len(customList)):
            if customList[i] > customList[j]:
                temp = customList[i]
                customList[i] = customList[j]
                customList[j] = temp
    return customList

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[j] < customList[min_index]:
                min_index = j
            
        temp = customList[i]
        customList[i] = customList[min_index]
        customList[min_index] = temp

    return customList

def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            #swapping the current element with previous element where i is previous and j is current
            temp = customList[i]
            customList[i] = customList[j]
            customList[j] = temp
    #replacing last element with current element
    temp = customList[i + 1]
    customList[i + 1] = customList[high]
    customList[high] = temp

    return (i + 1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)

        quickSort(customList, low, pi - 1)
        quickSort(customList, pi + 1, high)

def bucketSort(customList):
    numberOfBuckets = round(sqrt(len(customList)))
    maxValue = maximum(customList)
    arrsForSubArrs = []

    for i in range(numberOfBuckets):
        arrsForSubArrs.append([])
    for i in range(len(customList)):
        indexForBucket = ceil(customList[i] * numberOfBuckets / maxValue)
        arrsForSubArrs[indexForBucket - 1].append(customList[i])#append to that index the element
    for i in range(len(arrsForSubArrs)):
        arrsForSubArrs[i] = selectionSort(arrsForSubArrs[i])
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arrsForSubArrs[i])):
            customList[k] = arrsForSubArrs[i][j]
            k += 1

    return customList

def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    leftArray = [0] * n1
    rightArray = n2 *[0]
    for i in range(0, n1):
        leftArray[i] = customList[l + i]#copying elements to leftArray
    for i in range(0, n2):
        rightArray[i] = customList[m + 1 + i]#copying elements to rightArray starting from m + 1

    i = 0#initial index of leftArray
    j = 0#initil index of rightArray
    k = l#initial index in which elements will be sorted
    while i < n1 and j < n2:#till the indexes are smaller than the size of arrays
        if leftArray[i] < rightArray[j]:#if elements of leftArray are smaller
            customList[k] = leftArray[i]#copying element of leftArray to customList
            i += 1
        else:#if elements of rightArray are smaller
            customList[k] = rightArray[j]#copying elements of rightArray to customList
            j += 1
        k += 1

    while i < n1:
        customList[k] = leftArray[i]
        k += 1
        i += 1
    
    while j < n2:
        customList[k] = rightArray[j]
        k += 1
        j += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)

    return customList

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]#current element
        j = i - 1#previous index
        while j >= 0 and key < customList[j]:#if key is smaller than previous element
            customList[j + 1] = customList[j]#than previous element will become current element as j + 1 is current index
            j -= 1
        customList[j + 1] = key#otherwise current element will be key

    return customList

def heapify(customList, n, smallest):
    i = smallest
    l = 2 * smallest + 1
    r = 2 * smallest + 2
    if l < n and customList[l] <= customList[i]:#if the left element is smaller than smallest element
        i = l#then smallest element is l
    if r < n and customList[r] <= customList[i]:#if the right element is smaller than smallest element
        i = r
    if i != smallest:#if i is not smallest then swap i with smallest
        temp = customList[i]
        customList[i] = customList[smallest]
        customList[smallest] = temp

        heapify(customList, n, i)

def heapSort(customList):
    n = len(customList)
    for i in range(int(n // 2) - 1, -1, -1):
        heapify(customList, n, i)
    for i in range(n - 1, 0, -1):
        temp = customList[i]
        customList[i] = customList[0]
        customList[0] = temp

        heapify(customList, i, 0)

    return customList


cList = [8, 2, 4, 3, 1, 6, 5, 9, 7]
print("Original List: ", cList)
# bubbleSort(cList)
# selectionSort(cList)
# quickSort(cList, 0, 8)
# bucketSort(cList)
# mergeSort(cList, 0, 8)
# insertionSort(cList)
heapSort(cList)
print("Sorted List: ", cList)