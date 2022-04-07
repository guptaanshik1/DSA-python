myList = [1, 2, 3, 4]

def middle(lst):
    lst.remove(lst[0])
    lst.remove(lst[-1])
    return lst
            

print(middle(myList))