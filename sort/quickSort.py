def sortt(arr, low, high):
    if low >= high:
        return

    s, e = low, high
    m = s + (e - s) // 2
    pivot = arr[m]

    # swapping
    while s <= e:
        # when the below while conditions are violated then swap s and e
        while arr[s] < pivot:
            s += 1
        
        while arr[e] > pivot:
            e -= 1

        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    # the pivot will be right position in the sorted so the left and right around
    # pivot are required to be sorted
    sortt(arr, low, e)
    sortt(arr, s, high)

def quickSort(arr):
    sortt(arr, 0, len(arr) - 1)

arr = [5, 4, 3, 2, 1]
print(arr)
quickSort(arr)
print(arr)