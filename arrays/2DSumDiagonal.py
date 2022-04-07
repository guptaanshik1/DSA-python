myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if j == 1:
                # print(j)
                sum += a[i][j]
    return sum
        

print(sumDiagonal(myList2D))