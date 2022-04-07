arr, sums = [2, 3, 7, 8, 10], 12
size = len(arr)

t = []
for i in range(size + 1):
    temp = []
    for j in range(sums + 1):
        temp.append(True)
    t.append(temp)
# print(t)

def subsetSum(arr, sums, size):
    for i in range(size + 1):
        for j in range(sums + 1):
            if i == 0:
                t[i][j] = False
            elif j == 0:
                t[i][j] = True
    
            elif arr[i - 1] <= sums:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[size][sums]
            
print(subsetSum(arr, sums, size))