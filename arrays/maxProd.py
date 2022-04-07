def maxProduct(li):
    maxs = 0
    pairs = ""
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if (li[i] * li[j]) > maxs:
                maxs = li[i] * li[j]
                pairs = str(li[i]) + ", " + str(li[j])

    print(pairs)
    print(maxs)

li = [2, 4, 6, 8, 9, 1, 2, 4]
maxProduct(li)