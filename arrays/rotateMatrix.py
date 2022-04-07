def rotateMatrix(matrix):
    n = len(matrix)#number of rows in the matrix
    print(n)
    for i in matrix:
        print(i)
    for layer in range(int(n / 2)):#layer = 0
        first = layer
        print("first:", first)
        last = n - layer - 1#layer = 2 as 3 - 0 - 1 
        print("last:", last)

        for i in range(first, last):#from 0 to 2
            top = matrix[layer][i]#top = matrix[0][1 or 2]
            print("temp:", top)#1 and 2
            print("top:", matrix[layer][i])
            print("left:", matrix[-i - 1][layer])#left values in matrix: 4, 7
            matrix[layer][i] = matrix[-i - 1][layer]#matrix[-1 or -2 - 1][0] = matrix[-2 or -3]
            print("matrix[-3]:", matrix[-3])#entire row (7, 4, 1)
            print("matrix[-2]:", matrix[-2])#entire row (4, 5, 6)
            print("bottom:", matrix[-layer - 1][-i - 1])#matrix[0 - 1][- 1 or -2 - 1] = matrix[-1][-2 or -3]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            print("right:", matrix[i][-layer - 1])
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            matrix[i][-layer - 1] = top
    print("Rotated Matrix:")
    for i in matrix:
        print(i)
    


matrix = [ [1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9] ]

rotateMatrix(matrix)