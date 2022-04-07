def totalWays(stairs):
    if stairs < 0:
        return 0
    if stairs == 1 or stairs == 0:
        return 1
    return totalWays(stairs - 1) + totalWays(stairs - 2) + totalWays(stairs - 3)

print(totalWays(3))