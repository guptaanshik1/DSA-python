def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

custArray = [2, 5, 1, 4, 9, 10, 8, 9, 10]
print(linearSearch(custArray, 20))