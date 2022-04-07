def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1# j is previous element of i

        while j >= 0 and key < arr[j]:# run till a smaller previous element is not found or j is not 0
            arr[j + 1] = arr[j] # replace the element with greater element on previous
            j -= 1
        arr[j + 1] = key# place the greater element ahead of j

arr = [4, 5, 1, 2, 3]
print(arr)
insertionSort(arr)
print(arr)