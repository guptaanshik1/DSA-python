# index of pivot + 1 times array will be rotated

def findPivot(arr):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]: return mid
        if start < end and arr[mid] < arr[mid - 1]: return mid - 1
        if arr[start] > arr[mid]: end = mid - 1
        else: start = mid + 1
    return -1

def numberOfRotations(arr):
    pivot = findPivot(arr)
    if pivot != -1: return pivot + 1
    else: return 0

print(numberOfRotations([4, 5, 6, 7, 0, 1, 2]))

print(numberOfRotations([1, 2, 3, 4]))

# if there are duplicates in the array

# def findPivotWithDups(arr):
#     start, end = 0, len(arr) - 1

#     while start <= end:
#         mid = start + (end - start) // 2

#         if arr[mid] > arr[mid + 1]: return mid
#         if arr[mid] < arr[mid - 1]: return mid - 1

#         #if there are duplicates in the array
#         if arr[mid] == arr[start] == arr[end]:
#             if arr[start] > arr[start + 1]:# checking whether start is pivot or not
#                 return start
#             else: start = start + 1# skipping the duplicates by incrementing start
#             if arr[end] < aee[end - 1]:# checking whether end is pivot or not
#                 return end - 1
#             else: end = end - 1# skipping the duplicates by decrementing end

#         elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
#             start = start + 1
#         else: end = mid - 1

#     return -1