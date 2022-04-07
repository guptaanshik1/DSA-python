# matrix sorted as row sorted and column sorted

def searchMatrix(matrix, target):
    row, col = 0, len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        if matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    
    return [-1, -1]

print(searchMatrix(
    [
        [10, 20, 30, 40],
        [11, 25, 35, 45],
        [28, 29, 37, 49],
        [33, 34, 38, 50]
    ],
    37
))

def searchInRowsOfMatrix(matrix, row, colStart, colEnd, target):
    while colStart <= colEnd:
        mid = colStart + (colEnd - colStart) // 2
        if matrix[row][mid] == target:
            return [row, mid]
        if matrix[row][mid] < target:
            colStart = mid + 1
        else:
            colEnd = mid - 1
    return [-1, -1]

def searchSortedMatrix(matrix, target):
    row, col = len(matrix), 0
    if matrix: col = len(matrix[0])

    if row == 1:# if there is only 1 row
        # searching in only row and in the entire column
        return searchInRowsOfMatrix(matrix, 0, 0, col - 1, target)
        
    rowStart, rowEnd = 0, row - 1
    midCol = col // 2

    while rowStart < rowEnd - 1:# till the time this true there are all columns
        mid = rowStart + (rowEnd - rowStart) // 2# mid points to the middle row
        if matrix[mid][midCol] == target:# True if mid row and mid col element is target
            return [mid, midCol]
        if matrix[mid][midCol] < target:
            rowStart = mid
        else:
            rowEnd = mid
    
    # after the execution of mid there will be two rows

    # check whether the target is in the midCol
    if matrix[rowStart][midCol] == target:
        return [rowStart, midCol]
    if matrix[rowStart + 1][midCol] == target:
        return [rowStart + 1, midCol]

    # otherwise in the parts constructed

    # search in the first half
    if target <= matrix[rowStart][midCol - 1]:
        return searchInRowsOfMatrix(matrix, rowStart, 0, midCol - 1, target)

    # search in the second half
    if target >= matrix[rowStart][midCol + 1] and target <= matrix[rowStart][col - 1]:
        return searchInRowsOfMatrix(matrix, rowStart, midCol + 1, col - 1, target)

    # search in the third half
    if target <= matrix[rowStart + 1][midCol - 1]:
        return searchInRowsOfMatrix(matrix, rowStart + 1, 0, midCol - 1, target)

    # search in the fourth half
    else:
        return searchInRowsOfMatrix(matrix, rowStart + 1, midCol + 1, col - 1, target)
    

print(searchSortedMatrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], 4
))