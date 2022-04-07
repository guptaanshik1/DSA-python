def subsets(arr):
    outer = []
    outer.append([])
    for num in arr:
        n = len(outer)
        for i in range(n):# running inner loop till size of outer array
            inner = list(outer[i])# the inner loop will have elements of outer loop
            inner.append(num)# num is the elements of arr
            outer.append(inner)# appending the inner array to outer

    return outer

arr = [1, 2, 3]
# print(subsets(arr))

def subsetsDups(arr):# creating method subsetDups and passing arr as a parameter
    """
    if there is any duplicate subset then create the new subset starting
    from end of previous level's recursive call and this will only work if there are 
    adjacent duplicate elements in the array so for that purpose array 
    has to be sorted.
    """
    arr.sort()# sortting the array using sort function
    outer = []
    outer.append([])
    start, end = 0, 0
    for i in range(len(arr)):# looping through the array
        start = 0
        if i > 0 and arr[i] == arr[i - 1]:# if duplicate subset is present
            start = end + 1# then start from previous end + 1
        end = len(outer) - 1# end always has to be from the last subset
        n = len(outer)

        for j in range(start, n):# looping from start to length of outer array
            inner = list(outer[j])# creating an inner list which will initially have elements of outer array
            inner.append(arr[i])# appending the elements of array to inner list
            outer.append(inner)# appending the inner list to outer list
    return outer

ans = [1, 2, 2]
# size = int(input("Enter the size of the array: "))# taking input of size of array from user
# print("Enter the elements of the array: ")
# for i in range(size):# running a loop till size
#     el = int(input())# taking input of elements of array from the user
#     ans.append(el)# appending the elements to the ans list
print(subsetsDups(ans))# calling the method subsetsDups and passing ans list as an argument and printing the result