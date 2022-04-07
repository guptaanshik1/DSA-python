import random
# def permutation(li1, li2):
#     li2.reverse()
#     if li1 == li2:
#         return True
#     else:
#         return False

def permutation(li, li2):
    random.shuffle(li1)
    random.shuffle(li2)
    print("Shuffled li1:", li1)
    print("Shuffled li2:", li2)
    if li1 == li2:
        return True
    else:
        return False

li1 = [1, 2, 3, 4, 5]
li2 = [3, 2, 5, 1, 4]
print("Original li1:", li1)
print("Original li2:", li2)
print(permutation(li1, li2))