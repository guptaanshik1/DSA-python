def __helper(p, maze, row, col, path, steps):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        path[row][col] = steps# this is the last step so counting it as well
        for i in path:# printing path for the current recursive call
            print(i)
        print(p)
        print()
        return

    if not maze[row][col]: return

    maze[row][col] = False
    path[row][col] = steps# setting cell in path to current value of steps

    # steps will be incremented in each step
    if row < len(maze) - 1:
        __helper(p + 'D', maze, row + 1, col, path, steps + 1)
    if col < len(maze[0]) - 1:
        __helper(p + 'R', maze, row, col + 1, path, steps + 1)
    if row > 0:
        __helper(p + 'U', maze, row - 1, col, path, steps + 1)
    if col > 0:
        __helper(p + 'L', maze, row, col - 1, path, steps + 1)

    maze[row][col] = True# backtracking
    path[row][col] = 0# backtracking

def printPathMatrix(maze):
    path = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]
    return __helper("", maze, 0, 0, path, 1)

maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

printPathMatrix(maze)