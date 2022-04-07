wt, val = [10, 20, 30], [60, 100, 120]
w, size = 50, len(val)

t = []
for i in range(1000):
    temp = []
    for j in range(1000):
        temp.append(-1)
    t.append(temp)

print(t)

def knapsack(wt, val, w, size):
    if size == 0 or w == 0:
        return 0
    if t[size][w] != -1:
        return t[size][w]
    if wt[size - 1] > w:
        t[size][w] = knapsack(wt, val, w, size - 1)
        return t[size][w]
    else:
        t[size][w] = max(val[size - 1] + knapsack(wt, val, w - wt[size - 1], size - 1), knapsack(wt, val, w, size - 1))
        return t[size][w]

print(knapsack(wt, val, w, size))