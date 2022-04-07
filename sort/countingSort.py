def countingSort(arr):
    n = len(arr)
    mxEl = max(arr)
    count = [0] * (mxEl + 1)# as 0 to k is the range so k will be the max element
    result = [0] * n

    # store count of each element in the count array
    for i in range(n):
        count[arr[i]] += 1

    # count = [0, 1, 2, 2, 1, 1]
    # 0 = 0, 1 = 1, 2 = 2, 2 = 3, 1 = 4, 1 = 5
    # 0, 1, 2, 3, 4, 5 are indices and 0, 1, 2, 2, 1, 1 are number of times each element
    # in input array occurs
    
    # store the cumulative sum of count array
    for i in range(1, mxEl + 1):
        count[i] += count[i - 1]
    # print(count)
    # count = [0, 1, 3, 5, 6, 7]

    # find index of each element of the original array
    # and place element in result array
    i = n - 1
    while i >= 0:
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(n):
        arr[i] = result[i]

arr = [4, 9, 4, 7, 6, 1, 3, 7, 9]
print(arr)
countingSort(arr)
print(arr)