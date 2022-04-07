def helper(arr, idx, resEven, resOdd):
    if idx >= len(arr):
        return resEven + resOdd
    if arr[idx] % 2 == 0:
        resEven.append(arr[idx])
    elif arr[idx] % 2 != 0:
        resOdd.append(arr[idx])
    return helper(arr, idx + 1, resEven, resOdd)

def evenOdd(arr):
    idx, resEven, resOdd = 0, [], []
    return helper(arr, idx, resEven, resOdd)

print(evenOdd([12, 23, 21, 24, 4, 7, 8]))