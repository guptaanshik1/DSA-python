def orderAgnosticBS(arr, target):
    start, end = 0, len(arr) - 1

    # checking whether in ascending order or descending order
    isAsc = True if arr[start] <= arr[end] else False

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target: return mid
        
        if isAsc:
            if target < arr[mid]: end = mid - 1
            else: start = mid + 1

        else:
            if target < arr[mid]: start = mid + 1
            else: end = mid - 1

    return -1

print(orderAgnosticBS([90, 75, 18, 12, 6, 4, 3, 1], 18))