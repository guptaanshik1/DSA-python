def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    indexLast = len(coins) - 1
    while True:
        maxCoin = coins[indexLast]#last index will have greatest value as list is sorted

        if N >= maxCoin:
            print(maxCoin)
            N = N - maxCoin

        if N < maxCoin:
            indexLast -= 1

        if N == 0:
            break



def coinChangeProb(totalNumber, coins):
    coins.sort()
    N = totalNumber
    indexMax = len(coins) - 1
    while True:
        maxCoin = coins[indexMax]
        
        if N >= maxCoin:
            print(maxCoin)
            N = N - maxCoin

        if N < maxCoin:
            indexMax -= 1

        if N == 0:
            break




























coins = [1, 2, 5]
# coinChange(386, coins)
coinChangeProb(1200, coins)