from math import floor

def binarySearch(array, value):
    start = 0#pointer pointing 1st element
    end = len(array) - 1#pointer pointing the last element
    middle = floor((start + end) / 2)
    # print(start, middle, end)
    while array[middle] != value and start <= end:
        if array[middle] < value:
            start = middle + 1
        else:
            end = middle - 1
        middle = floor((start + end) / 2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1

custArray = [5, 1, 6, 15, 3, 7, 9]
print(binarySearch(custArray, 6))
custArray.sort()
print(binarySearch(custArray, 6))