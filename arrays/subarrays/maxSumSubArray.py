def maxSumSubArray(arr, n):
    maxSum = 0
    for i in range(len(arr)):# i is starting point
        for j in range(i, len(arr)):# j is ending point
            sm = 0
            for k in range(i, j + 1):# k is from i to j
                # print(arr[k], end=' ')
                sm += arr[k]
            # print()
            maxSum = max(maxSum, sm)

    return maxSum


arr = [-1, 4, 7, 2]
print(maxSumSubArray(arr, len(arr)))