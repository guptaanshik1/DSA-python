def countingSort(arr, place):
    n = len(arr)
    count = [0] * 10# digits can be only from 0 to 9
    result = [0] * n

    # calculate count of each element in the array based on unit place
    for i in range(n):
        index = arr[i] // place# dividing with ones, tens ....
        count[index % 10] += 1# and adding that to count index according to occurence

    # storing the cumulative sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // place
        result[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = result[i]

def radixSort(arr):
    
    # find the maximum element then according to the number of digits of maximum
    # number the number of times counting sort has to be applied
    mxEl = max(arr)
    
    place = 1
    while mxEl // place > 0:
        countingSort(arr, place)
        place *= 10# to change from one's place to tens place ....

arr = [329, 457, 657, 839, 436, 720, 355]
print(arr)

radixSort(arr)
print(arr)