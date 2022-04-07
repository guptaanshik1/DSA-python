def missingNumber(myList, totalCount):
    totalCount = len(myList) + 1
    sum1 = int((totalCount * (totalCount + 1)) / 2)
    sum2 = sum(myList)
    diff = sum1 - sum2
    return diff

print(missingNumber([1, 2, 3, 4, 6], 6))