def firstOccurence(arr, target):
    start, end = 0, len(arr) - 1
    first = 0
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            first = mid
            end = mid - 1
        elif arr[mid] > target: end = mid - 1
        else: start = mid + 1
    return first

def lastOccurence(arr, target):
    start, end = 0, len(arr) - 1
    last = 0
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            last = mid
            start = mid + 1
        elif arr[mid] > target: end = mid - 1
        else: start = mid + 1
    return last

def countOccurences(arr, target):
    if target not in arr: return -1
    
    first = firstOccurence(arr, target)
    last = lastOccurence(arr, target)
    return last - first + 1

print(countOccurences([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 6))