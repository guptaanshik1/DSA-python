def helper1(arr, index, key):
    if index >= len(arr):
        return -1
    if arr[index] == key:
        return index
    return helper1(arr, index + 1, key)

def firstOcc(arr, key):
    index = 0
    return helper1(arr, index, key)

def helper2(arr, index, key):
    if index <= 0:
        return -1
    if arr[index] == key:
        return index
    return helper2(arr, index - 1, key)

def lastOcc(arr, key):
    index = len(arr) - 1
    return helper2(arr, index, key)

print(firstOcc([4, 2, 1, 2, 5, 2, 7], 2))
print(lastOcc([4, 2, 1, 2, 5, 2, 7], 2))