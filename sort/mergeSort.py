def mergeSort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2

    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(nums, left, right)

def merge(nums, left, right):
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums

arr = [8, 3, 4, 12, 5, 6]
arr2 = [5, 2, 3, 1]

print(arr2)
print(mergeSort(arr2))