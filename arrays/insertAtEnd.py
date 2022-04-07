def insertAtPos(arr, capacity, n, pos, element):
    if n == capacity:
        return n
    index = pos - 1
    for i in range(n - 1, index + 1, -1):
        arr[i + 1] = arr[i]
    arr[index] = element

arr = [5, 10, 13, 11]
capacity = 6
n = len(arr)

print(arr)
insertAtPos(arr, capacity, n, 1, 15)

print(arr)