def searchTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return "The element does exist in the tuple"

#creating
myTuple1 = 1, 2, 3, 4
myTuple2 = (1, 2, 3, 4)
myTuple3 = tuple("1234")#only string can be passed
myTuple4 = (1, )#tuple with only one element

print(myTuple1)
print(myTuple2)
print(myTuple3)
print(myTuple4)

#accessing
print(myTuple1[1], myTuple1[-1], myTuple1[1:], myTuple1[-1:])

#traverse
for i in myTuple1:
    print(i, end=" ")

for i in range(len(myTuple1)):
    print(myTuple1[i], end=" ")

print()
#Searching
print(searchTuple(myTuple1, 4))

#######################################

#Operators

#in operator
print(2 in myTuple1)

# * operator
print(myTuple2 * 2)

#Concatination of two lists with +(concatination) operator
print(myTuple1 + myTuple2)

#######################################

#Methods

#count
print(myTuple1.count(2))

#index
print(myTuple1.index(2))

########################################

#len
print(len(myTuple1))

#max
print(max(myTuple1))

#min
print(min(myTuple1))

#tuple
print(tuple(['a', 'b', 'c', 'd']))

#########################################

myTuple5 = (1, 2, (1, 2), [3, 4], 3, 4)
print(myTuple5)