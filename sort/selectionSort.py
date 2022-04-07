def maxIndex(arr, start, end):
    mx = start
    for i in range(start, end + 1):
        if arr[start] < arr[i]:
            mx = i
    return mx

# keep finding the element on the max index
# then keep swapping that element with the last index
def selectionSort(arr):
    for i in range(len(arr)):
        lastIndex = len(arr) - i - 1
        mxEl = maxIndex(arr, 0, lastIndex)
        arr[mxEl], arr[lastIndex] = arr[lastIndex], arr[mxEl]

arr = [5, 4, 1, 2, 3]

print(arr)
selectionSort(arr)
print(arr)