arr = [2, 3, 5, 6, 8, 10]
size, sums = len(arr), 10

t = []
for i in range(size + 1):
    temp = []
    for j in range(sums + 1):
        temp.append(0)
    t.append(temp)

# print(t)

def countSubsets(arr, size, sums):
    for i in range(size + 1):
        for j in range(sums + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1

            if arr[size - 1] < sums:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[size][sums]

print(countSubsets(arr, size, sums))