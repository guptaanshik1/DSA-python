arr = [1, 5, 11, 5]
# arr = [1, 5, 11, 5]
size = len(arr)
# sums = 10

def isSubsetSum(arr, size, sums):
    if sums == 0:
        return True
    if size == 0 and sums != 0:
        return False
 
    if arr[size-1] > sums:
        return isSubsetSum(arr, size-1, sums)
 
    return isSubsetSum(arr, size-1, sums) or isSubsetSum(arr, size-1, sums-arr[size-1])

def equalSumPartition(arr, size):
    sums = 0
    sums = sum(arr)
    if sums % 2 != 0:
        return False
    elif sums % 2 == 0:
        return isSubsetSum(arr, size, sums // 2)

# print(isSubsetSum(arr, size, sums))
print(equalSumPartition(arr, size))