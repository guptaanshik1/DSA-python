def maxHouses(houses, currentHouse):
    if currentHouse > len(houses):
        return 0
    else:
        stealFromFirst = houses[currentHouse] + maxHouses(houses, currentHouse + 2)#taking third house after 1st so + 2
        skippingFirst = maxHouses(houses + currentHouse + 1)#start from second house
        return max(stealFromFirst, skippingFirst)

houses = [6, 7, 1, 30, 8, 2, 4]
print(maxHouses(houses, 0))