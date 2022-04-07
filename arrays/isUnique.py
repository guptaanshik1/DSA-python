def is_unique(li):
    emptyLi = []
    for i in li:
        if i in emptyLi:
            print(i)
            continue
            return False
        else:
            emptyLi.append(i)
    return True

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_unique(li))