def numberFactor(n):
    if n in (0, 1, 2):
        return 1#if n is 0, 1, 2 then only 1 factor to form 2
    elif n == 3:
        return 2#if n is 0, 1, 2 then only 2 factor to form 3 which are (1, 2), (2, 1)
    else:
        subP1 = numberFactor(n - 1)
        subP2 = numberFactor(n - 3)
        subP3 = numberFactor(n - 4)
        return subP1 + subP2 + subP3

print(numberFactor(4))