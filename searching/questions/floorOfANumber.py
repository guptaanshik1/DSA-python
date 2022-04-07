def ceil(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target: return arr[mid]

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return end



arr, target = [2, 3, 5, 9, 14, 16, 18], 15
print(ceil(arr, target))



"""
14 is answer because after some iterations s, e, m will be pointing
to 14 which is smaller than target and in the next iteration 
start will be pointing to end + 1 which is 16 and the loop 
will break.
As floor is the greatest number smaller than target
"""