#if all the pairs are required
def findPairsAll(li, target):
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                print(li[i], " + ", li[j], " = ", target)

# if only distinct pairs are required
def findPairsDistinct(li, target):
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] == li[j]:
                continue
            elif li[i] + li[j] == target:
                print(i, j)
                print(li[i], " + ", li[j], " = ", target)

li = [1, 2, 3, 2, 3, 4, 5, 6]
# findPairsAll(li, 5)
print()
findPairsDistinct(li, 6)