import math

def binarySearchIter(arr, value):
    left, right = 0, len(arr) - 1
    mid = math.floor((left + right) / 2)

    while arr[mid] != value and left <= right:
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
        mid = math.floor((left + right) / 2)

    if arr[mid] == value:
        return mid
    else:
        return -1

def helper(arr, left, right, val):
    if left > right:
        return -1
    mid = math.floor((left + right) / 2)
    if arr[mid] == val:
        return mid
    if arr[mid] > val:
        return helper(arr, left, mid - 1, val)
    if arr[mid] < val:
        return helper(arr, mid + 1, right, val)
    
def binarySearchRec(arr, val):
    left, right = 0, len(arr) - 1
    return helper(arr, left, right, val)

custArray = [5, 1, 6, 15, 3, 6, 9]
print(binarySearchIter(custArray, 6))
print(binarySearchRec(custArray, 6))