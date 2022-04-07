def kthGrammar(n, k):
    if n == 1 or k == 1:
        return 0
    mid = pow(2, n - 1) / 2
    if mid >= k:
        return kthGrammar(n - 1, k)
    else:
        res = kthGrammar(n - 1, k - mid)
        if res == 0:
            return 1
        else:
            return 0

print(kthGrammar(3, 1))