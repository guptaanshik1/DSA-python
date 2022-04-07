def helper(arr, index, p):
    if index >= len(arr):
        return p
    p = p * arr[index]
    return helper(arr, index + 1, p)

def productOfArray(arr):
    index, p = 0, 1
    return helper(arr, index, p)

arr = [1, 2, 3, 10]
print(productOfArray(arr))