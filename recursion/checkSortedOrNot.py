arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 4, 2, 11]

def checkArray(arr, index):
    if index >= len(arr):
        return True
    if arr[index] < arr[index - 1]:
        return False
    return checkArray(arr, index + 1)

def sortedOrUnsorted(arr):
    if checkArray(arr, 1):
        print("The Array is sorted")
    else:
        print("The Array is unsorted")

sortedOrUnsorted(arr1)
sortedOrUnsorted(arr2)