import array as arr

#accessing
def access(arr, index):
    if index >= len(arr):
        print("There is no such index in array")
    else:
        print(arr[index])

#searching
def search(arr, value):
    flag = 0
    for i in arr:
        if value == i:
            flag = 1
            break
    if flag == 1:
        print("found")
    else:
        print("not found")

arr1 = arr.array('i', [1, 2, 3, 4, 5, 6])#create
arr1.insert(2, 22)

for i in arr1:#traversing
    print(i)
print("\n")

access(arr1, 3)#accessing

print("\n")

print(search(arr1, 6))

arr1.remove(5)

print(arr1)


#####################################################################
print("2nd part")
arr2 = arr.array('i', [10, 11, 12, 13, 14, 15, 16])
arr2.append(17)#append
print(arr2)

#extend array
arr2.extend(arr1)
print(arr2)

#appending a list to array
li = [1, 2]
arr2.fromlist(li)
print(arr2)

arr2.remove(1)
print(arr2)

#removing using the pop function
arr2.pop()
print(arr2)

#index
print(arr2.index(1))

#status of array using buffer_info()
print(arr2.buffer_info())

#converting array to list
print(arr2.tolist())
