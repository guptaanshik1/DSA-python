class Solution:
    def __queen(self, board, row):
        if row == len(board):
            self.__display(board)
            print()
            return 1

        count = 0

        # placing the queen starting from the 0th column
        for col in range(len(board)):
            if self.__isSafe(board, row, col):# if safe
                board[row][col] = True# then queen can be placed
                count += self.__queen(board, row + 1)# check for other rows then
                board[row][col] = False # backtracking

        return count

    def __isSafe(self, board, row, col):
        # checking in the vertical row by keeping the column same
        for i in range(len(board)):
            if board[i][col] == True:# that means if already queen is present in the vertical row
                return False
            
        # checking for the left diagnol
        maxTimeGoLeft = min(row, col)
        for i in range(1, maxTimeGoLeft + 1):
            if board[row - i][col - i] == True:
                return False

        # checking for the right diagnol
        maxTimeGoRight = min(row, len(board) - col - 1)
        for i in range(1, maxTimeGoRight + 1):
            if board[row - i][col + i]:
                return False

        return True# if checks fails then safe to place

    def __display(self, board):
        for row in board:
            for el in row:
                if el:
                    print("Q", end = " ")
                else:
                    print(".", end = " ")
            print()

    def solveNQueens(self, n):
        board = [[None for j in range(n)] for i in range(n)]
        return self.__queen(board, 0)

sol = Solution()
print(sol.solveNQueens(4))