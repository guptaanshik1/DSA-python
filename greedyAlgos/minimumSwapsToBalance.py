# def numberOfSwaps(s):
#     countLeft, countRight, imbalance, swaps = 0, 0, 0, 0
    
#     for i in range(len(s)):
#         if s[i] == '[':
#             countLeft += 1
#             if imbalance > 0:
#                 swaps += imbalance
#                 imbalance -= 1

#         elif s[i] == ']':
#             countRight += 1
#             imbalance = countRight - countLeft

#     return swaps

# s1 = '[]][]['
# s2 = '[]'
# s3 = ']][['
# print(numberOfSwaps(s1))

def zip1(li1, li2): # creating the method zip and passing lists li1 and li2 as parameters
    i, j = 0, 0
    res = []
      
    # running a loop till i is less than length of li1 and j is less than length of li2
    while i < len(li1) and j < len(li2):
        res.append((li1[i], li2[j])) # appeding current elements of both lists to res as a tuple
        i += 1 # incrementing value of i with 1
        j += 1 # incrementing value of j with 1
      
    return res # returning the res list from the method
  
li1, li2 = ['a', 'b', 'c'], [1, 2, 3]
  
print(zip1(li1, li2)) # calling the method zip1 and passing li1 and li2 as arguments and printing result