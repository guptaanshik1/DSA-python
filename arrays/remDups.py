def removeDuplicates(myList):
    li = []
    for i in range(len(myList)):
        if myList[i] in li:
            continue
        else:
            li.append(myList[i])
    return li


print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))