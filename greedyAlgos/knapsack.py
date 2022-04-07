class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def knapsackMethod(items, capacity):
    items.sort(key = lambda x: x.ratio, reverse = True)
    usedCapacity = 0
    totalValue = 0

    for i in items:
        if usedCapacity + i.weight <= capacity:#if used capacity with current item's weight is less than total capacity
            usedCapacity += i.weight
            totalValue = i.value

        else:
            unusedCapacity = capacity - usedCapacity
            value = i.ratio * unusedCapacity
            usedCapacity += unusedCapacity
            totalValue += value

        if usedCapacity == 0:
            break

    print("Total value obtained:", totalValue)

item1 = Item(100, 20)
item2 = Item(120, 30)
item3 = Item(60, 10)

knapsackMethod([item1, item2, item3], 50)