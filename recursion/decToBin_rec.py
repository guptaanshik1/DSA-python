def decToBin(n):
    assert int(n) == n, "The number must be an integer only"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decToBin(int(n / 2))

print(decToBin(20))