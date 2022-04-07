myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]

def firstSecond(givenList):
    maxs = 0
    pair = 0
    for i in range(len(givenList)):
        for j in range(i + 1, len(givenList)):
            if (givenList[i] * givenList[j]) > maxs:
                maxs = givenList[i] * givenList[j]
                pair = givenList[j], givenList[i]

    return pair

print(firstSecond(myList))