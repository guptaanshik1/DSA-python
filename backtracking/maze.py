# from (3, 3)
def countPaths(row, col):
    if row == 1 or col == 1:# 1 will be the last column and row
        return 1# when one of them becomes 1 that means 1 answer

    left = countPaths(row - 1, col)# going down
    right = countPaths(row, col - 1)# going right

    return left + right

print(countPaths(3, 3))

def __helperPaths(p, row, col):
    if row == 1 and col == 1:
        print(p)
        return

    if row > 1:
        __helperPaths(p + 'D', row - 1, col)
    if col > 1:
        __helperPaths(p + 'R', row, col - 1)

def printPaths(row, col):
    return __helperPaths("", row, col)

printPaths(3, 3)

def __helperPathsReturn(p, row, col):
    if row == 1 and col == 1:
        ans = []
        ans.append(p)
        return ans

    ans = []
    if row > 1:
        ans.extend(__helperPathsReturn(p + 'D', row - 1, col))
    if col > 1:
        ans.extend(__helperPathsReturn(p + 'R', row, col - 1))
    
    return ans

def returnPaths(row, col):
    return __helperPathsReturn("", row, col)

print(returnPaths(3, 3))

def __helperPathsWithRestrictions(p, maze, row, col):
    # note maze is a boolean array
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        print(p)
        return

    if maze[row][col] == False:
        return

    if row < len(maze) - 1:
        __helperPathsWithRestrictions(p + 'D', maze, row + 1, col)
    if col < len(maze[0]) - 1:
        __helperPathsWithRestrictions(p + 'R', maze, row, col + 1)

def printPathsWithRestrictions(maze):
    return __helperPathsWithRestrictions("", maze, 0, 0)

maze1 = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

print("*********With restrictions**********")
printPathsWithRestrictions(maze1)

print("********With diagnol movement answer********")
def __helperDiagnol(p, maze, row, col):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        ans = []
        ans.append(p)
        return ans

    ans = []

    if row < len(maze) - 1:
        ans.extend(__helperDiagnol(p + 'V', maze, row + 1, col))
    if col < len(maze[0]) - 1:
        ans.extend(__helperDiagnol(p + 'H', maze, row, col + 1))
    if row < len(maze) - 1 and col < len(maze[0]) - 1:
        ans.extend(__helperDiagnol(p + 'D', maze, row + 1, col + 1))

    return ans

def diagnolPaths(maze):
    return __helperDiagnol("", maze, 0, 0)

maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

print(diagnolPaths(maze))

print("******backtracking******")

def __helperAllPaths(p, maze, row, col):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        print(p)
        return

    if not maze[row][col]: return# the visited cells will be returned

    maze[row][col] = False

    # going down
    if row < len(maze) - 1:
        __helperAllPaths(p + 'D', maze, row + 1, col)
    # going right
    if col < len(maze[0]) - 1:
        __helperAllPaths(p + 'R', maze, row, col + 1)
    # going up
    if row > 0:
        __helperAllPaths(p + 'U', maze, row - 1, col)
    # going left
    if col > 0:
        __helperAllPaths(p + 'L', maze, row, col - 1)

    """
    Here all the functions call ends and as the original mae array has been
    modified so before removing the function call restoring the changes
    """
    maze[row][col] = True

def allPaths(maze):
    return __helperAllPaths("", maze, 0, 0)

print()
allPaths(maze)

def __helperAllPathsReturn(p, maze, row, col):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        ans = []
        ans.append(p)
        return ans

    ans = []

    if not maze[row][col]: return ans

    maze[row][col] = False

    if row < len(maze) - 1:
        ans.extend(__helperAllPathsReturn(p + 'D', maze, row + 1, col))
    if col < len(maze[0]) - 1:
        ans.extend(__helperAllPathsReturn(p + 'R', maze, row, col + 1))
    if row > 0:
        ans.extend(__helperAllPathsReturn(p + 'U', maze, row - 1, col))
    if col > 0:
        ans.extend(__helperAllPathsReturn(p + 'L', maze, row, col - 1))

    maze[row][col] = True

    return ans

def allPathsReturn(maze):
    return __helperAllPathsReturn("", maze, 0, 0)

print(allPathsReturn(maze))