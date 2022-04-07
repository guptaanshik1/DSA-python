def towerOfHanoi(n, src, dest, helper):
    if n == 0:
        return
    towerOfHanoi(n - 1, src, helper, dest)
    print("Move from", src, "to", dest)
    towerOfHanoi(n - 1, helper, dest, src)

towerOfHanoi(3, 'A', 'C', 'B')