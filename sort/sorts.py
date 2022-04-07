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
    i = low - 1#starting from 0 as i is 1st index
    pivot = customList[high]#last element is pivot
    for j in range(low, high):
        if customList[j] <= pivot:#the case of right marker where element is smaller or equal to pivot
            i += 1#increasing the marker to move

            #when an element greater than pivot is found swap the element with jth element
            temp = customList[i]
            customList[i] = customList[j]
            customList[j] = temp
    #replacing with pivot the current element
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
    arrForSubArrs = []
    
    for i in range(numberOfBuckets):
        arrForSubArrs.append([])#numberOfBuckets = number of sub arrays in arr
    for j in customList:
        indexInBucket = ceil(j * numberOfBuckets / maxValue)
        arrForSubArrs[indexInBucket - 1].append(j)
    for i in range(numberOfBuckets):
        arrForSubArrs[i] = selectionSort(arrForSubArrs[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arrForSubArrs[i])):
            customList[k] = arrForSubArrs[i][j]
            k += 1

    return customList

def merge(customList, l, m, r):
    n1 = m - l + 1#n1 is number of elements in left array
    n2 = r - m#n2 is number of elements in right array
    L = [0] * n1
    R = n2 * [0]
    for i in range(0, n1):
        L[i] = customList[l + i]
    for i in range(0, n2):
        R[i] = customList[m + 1 + i]
    
    i = 0#initial index of left array
    j = 0#initial array of right array
    k = l#initial index of new array to which the elements will be merged
    while i < n1 and j < n2:
        if L[i] <= R[j]:#if values of left array are smaller then add to array
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]#if values of right array are smaller then add to array
            j += 1
        k += 1

    #adding remaining elements from left array
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    #adding remaining elements from right array
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)#m + 1 because the element next of m
        merge(customList, l, m, r)

def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    if smallest != i:
        temp = customList[i]
        customList[i] = customList[smallest]
        customList[smallest] = temp

        heapify(customList, n, smallest)

def heapSort(customList):
    n = len(customList)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)
    for i in range(n - 1, 0, -1):
        temp = customList[i]
        customList[i] = customList[0]
        customList[0] = temp
        heapify(customList, i, 0)

def insertionSort(customList):
    for i in range(1, len(customList)):#starting from 1 as from 1st element has to move to sorted array first
        key = customList[i]
        j = i - 1#previous element
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]#inserting in the sorted position
            j -= 1#moving j again 1 step back
        customList[j + 1] = key#inserting in the current position
    return customList

cList = [2, 4, 1, 3, 6, 9, 8, 7, 5]
# print(bubbleSort(cList))
# print(selectionSort(cList))
# quickSort(cList, 0, 8)
# bucketSort(cList)
# mergeSort(cList, 0, 8)
# heapSort(cList)
insertionSort(cList)
print(cList)