li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def find(li, value):
    flag = 0
    index = 0
    for i in range(len(li)):
        if li[i] == value:
            flag = 1
            index = i
            break
    if flag == 1:
        print(index)
    else:
        print("The element does not found")

find(li, 12)