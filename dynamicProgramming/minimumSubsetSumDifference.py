import sys

arr = [1, 6, 11, 5]

def MSSD(arr):
    t, vec = [], []
    for i in range(len(arr) + 1):
        temp = []
        for j in range(sum(arr) + 1):
            temp.append(0)
        t.append(temp)

    for i in range(len(arr) + 1):
        t[i][0] = True
    for j in range(1, sum(arr) + 1):
        t[0][j] = False

    for i in range(len(arr) + 1):
        for j in range(sum(arr) + 1):
            if arr[i - 1] <= sum(arr):
                t[i][j] = t[i - 1][j] or t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    # print(len(t) - 1)
    for i in range(len(t)):
        for j in range(len(t[i]) // 2):
            if i == 3 and t[i][j]:
                vec.append(j)
    
    mn = sys.maxsize
    for i in range(len(vec)):
        mn = min(mn, sum(arr) - 2 * vec[i])
    return mn

print(MSSD(arr))