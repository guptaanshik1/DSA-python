def printSubArrays(arr, n):
    for i in range(len(arr)):# i is starting point
        for j in range(i, len(arr)):# j is ending point
            for k in range(i, j + 1):# k is from i to j
                print(arr[k], end=' ')
            print()


arr = [-1, 4, 7, 2]
printSubArrays(arr, len(arr))