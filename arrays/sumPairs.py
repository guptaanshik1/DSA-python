def pairSum(myList, sum):
    li = []
    pairs = ''
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if (myList[i] + myList[j]) == sum:
                pairs = str(myList[i]) + " + " + str(myList[j])
                li.append(pairs)
    return(li)


print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))