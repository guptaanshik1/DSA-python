import numpy as np

#searching
def search(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return "The value is located at" + str(i) + " " + str(j)
            else:
                return "The element is not found"

arr2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(arr2D)

newArr2D = np.insert(arr2D, 0, [[0, 0, 0, 0]], axis = 0)#adding row
print(newArr2D)

newArr2D = np.insert(arr2D, 0, [[0, 0, 0, 0]], axis = 1)##adding column
print(newArr2D)

np.append(arr2D, [[0, 0, 0, 0]], axis = 0)#adding always at the last

#accessing elements
def access(arr, rowIndex, colIndex):
    if rowIndex >= len(arr) and colIndex >= len(arr[0]):
        print("Incorrect index")
    else:
        print(arr[rowIndex][colIndex])

access(arr2D, 1, 2)

#traversing
for i in range(len(arr2D)):
    for j in range(len(arr2D[0])):
        print(arr2D[i][j])

def search(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return "The value is located at" + str(i) + " " + str(j)
            else:
                return "The element is not found"

search(arr2D, 4)

#delete
add2DDelete = np.delete(arr2D, 0, axis = 0)