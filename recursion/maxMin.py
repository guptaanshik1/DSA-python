def solveMax(arr, index, mx):
    if index >= len(arr):
        return mx
    if arr[index] > mx:
        mx = arr[index]
    return solveMax(arr, index + 1, mx)

def maxx(arr):
    index, mx = 0, arr[0]
    return solveMax(arr, index, mx)

arr = [12, 1234, 45, 67, 1]

print(maxx(arr))

def solveMin(arr, index, mn):
    if index >= len(arr):
        return mn
    if arr[index] < mn:
        mn = arr[index]

    return solveMin(arr, index + 1, mn)

def minn(arr):
    index, mn = 0, arr[0]
    return solveMin(arr, index, mn)

print(minn(arr))