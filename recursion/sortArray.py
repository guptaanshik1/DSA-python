def sortt(arr):
    # single element is always sorted in array
    if len(arr) == 1:
        return

    temp = arr[len(arr) - 1]
    arr.pop()# popping the last element
    sortt(arr)# calling function for smaller input
    insertt(arr, temp)# inserting the popped element at sorted place in remaining array
    return arr

def insertt(arr, temp):
    # is array is empty or last element is smallet than element to be inserted
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return

    value = arr[len(arr) - 1]# fetching the last element to add it in the last
    arr.pop()# popping that element from array
    insertt(arr, temp)# calling function for smaller input
    arr.append(value)# appending the popped element back
    return arr

print(sortt([0, 5, 1, 2, 10, 9]))