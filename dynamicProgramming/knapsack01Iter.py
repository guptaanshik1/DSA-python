wt, val = [10, 20, 30], [60, 100, 120]
w, size = 50, len(val)

t = []

for i in range(size + 1):
    temp = []
    for j in range(w + 1):
            temp.append(0)
    t.append(temp)

def knapsack(wt, val, w, size):
    for i in range(size + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[size - 1] < w:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[size][w]

print(knapsack(wt, val, w, size))